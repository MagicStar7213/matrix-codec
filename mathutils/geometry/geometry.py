from sympy import Symbol, parse_expr, Equality, Expr, Point3D, solve, Plane, Line3D
from sympy.abc import x, y ,z
from sympy.parsing.sympy_parser import T
from mathutils.geometry.relative_positions import relpos
from mathutils.parser import construct_string, safe_eval
import re


def main():
    env = { 'classes': [Plane, Line3D, Point3D],
            'whitelist': [],
            'vars': {}}
    print("""
 _  _  _ | _|_. _   _  _  _  _ _  _ _|_ _ 
(_|| |(_||\\/| |(_  (_|(/_(_)| | |(/_ | |\\/
          /         _|                  /  """)
    while True:
        raw = input('>> ')
        if raw == 'q':
            return
        if re.match(r'relpos \w+,\w+(,\w)?', raw):
            split = raw.removeprefix('relpos ').split(',')
            geom: list[Line3D | Plane] = []
            for geomid in split:
                processed, env = process_geometry(geomid, env)
                if processed:
                    geom.append(processed)
            print(relpos(*geom))
        elif raw.replace(' ','') == '':
            pass
        else:
            processed, env = process_geometry(raw, env)
            ... # TODO: Implement logic

def str_to_list(raw: str) -> list[str | list] | tuple[str,list[Expr]]:
    parsed: list[str | list] = []
    if re.match(r'([A-Z]+\(-?\d(\.\d+)?,-?\d(\.\d+)?(,-?\d(\.\d+)?)?\))', raw):
        separated = raw.split('(')
        separated[-1] = separated[-1].removesuffix(')')
        point = (separated[0], list(map(parse_expr, separated[-1].split(','))))
        return point
    for char in raw:
        parsed.append(char)
        if char == ':':
            parsed = [''.join(list(map(str, parsed[:-1]))), '=']
            parsed[-1] = '='
            parsed.append(raw[raw.index(char) + 1:].split(','))
            break
    return parsed

def get_plane(eq: Equality) -> Plane:
    def_point:dict[Symbol,(int | Expr)] = {x:0,y:0,z:0}
    coeffs: list[tuple[Symbol, Expr]] = [(i, eq.lhs.coeff(i)) for i in [x, y, z] if eq.lhs.coeff(i) != 0] # type: ignore
    if len(coeffs) == 1:
        var = coeffs[0][0]
        point = def_point.copy()
        point.update({var: solve(eq.subs(*[(i, 0) for i in [x, y, z] if i != var]))[0]})
        p1 = Point3D(*[v for (_,v) in point.items()])
    elif len(coeffs) == 2:
        vars = [i[0] for i in coeffs]
        point = def_point.copy()
        point.update({vars[1]: solve(eq.subs([(i, 0) for i in [x, y, z] if i != vars[1]]), vars[1])[0]})
        p1 = Point3D(*[v for (_, v) in point.items()])
    else:
        p1 = Point3D(0,0, solve(eq.subs([(x,0),(y,0)]),z)[0])
    
    return Plane(p1, normal_vector=(eq.lhs.coeff(x), eq.lhs.coeff(y), eq.lhs.coeff(z))) # type: ignore

def parse_equations(raw: list[str | list] | tuple[str, list[Expr]], env: dict):
    parsed: list[str | list | Point3D | Line3D | Plane] = []
    parsed += list(raw).copy()
    if isinstance(raw, tuple):
        parsed.insert(-1, '=')
        parsed[-1] = Point3D(*raw[1])
    else:
        if construct_string(raw) in env['vars']:
            return construct_string(raw)
        else:
            transformations = T[1:5]+T[6]+T[8]+T[7]+T[9:]
            raw_equations: list[Equality] = [parse_expr(eq, transformations=transformations) for eq in raw[-1]]
            equations: list[Equality] = [Equality(eq.lhs - eq.rhs,0) for eq in raw_equations] # type: ignore
            if len(equations) == 1:
                eq = equations[0]
                parsed[-1] = get_plane(eq)
            elif len(equations) == 2:
                line = get_plane(equations[0]).intersection(get_plane(equations[1]))
                parsed[-1] = '' if not line else line[0] # type: ignore
            else:
                raise ValueError('Objects defined by more than 2 equations are not supported')
    return list(map(str, parsed))

def process_geometry(raw: str, env: dict) -> tuple[Line3D | Plane | None, dict]:
    try:
        equations = parse_equations(str_to_list(raw), env)
        parsed, env = safe_eval(equations if isinstance(equations,str) else construct_string(equations), env) # type: ignore
    except SyntaxError as e:
        print(f'Syntax error: {e}')
        return None, env
    except TypeError as e:
        print(f'Type error: {e}')
        return None, env
    except ValueError as e:
        print(f'Value error: {e}')
        return None, env
    except NameError as e:
        print(f'Name error: {e}')
        return None, env
    else:
        return parsed, env