from sympy import parse_expr, Equality, Expr, Point3D, solve, Plane, Line3D
from sympy.abc import x, y ,z
from sympy.geometry.entity import GeometryEntity
from sympy.parsing.sympy_parser import T
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
        else:
            processed, env = process_geometry(raw, env)
            ... # TODO: Implement logic

def str_to_list(raw: str) -> list[str | list]:
    parsed: list[str | list] = []
    if re.match(r'([A-Z]+\(-?\d(\.\d+)?,-?\d(\.\d+)?(,-?\d(\.\d+)?)?\))', raw):
        separated = raw.split('(')
        separated[-1] = separated[-1].removesuffix(')')
        parsed = [separated[0], list(map(parse_expr, separated[-1].split(',')))]
        return parsed
    for char in raw:
        parsed.append(char)
        if char == ':':
            parsed = [''.join(list(map(str, parsed[:-1]))), '=']
            parsed[-1] = '='
            parsed.append(raw[raw.index(char) + 1:].split(','))
            break
    return parsed

def get_plane(eq: Equality) -> Plane:
    p1 = Point3D(0, 0, solve(eq.subs(x, 0).subs(y, 0), z)[0])
    return Plane(p1, normal_vector=(eq.lhs.coeff(x), eq.lhs.coeff(y), eq.lhs.coeff(z)))

def parse_equations(raw: list[str | list], env: dict):
    parsed: list[str | Point3D | Line3D | Plane] = []
    parsed += raw.copy()
    if construct_string(raw) in env['vars']:
        return construct_string(raw)
    if len(raw) == 2 and type(raw[0]) is str and type(raw[1]) is list and len(raw[1]) == 3 and all(isinstance(i, Expr) for i in raw[1]):
        parsed.insert(-1, '=')
        parsed[-1] = Point3D(*raw[1])
    else:
        transformations = T[1:5]+T[6]+T[8]+T[7]+T[9:]
        equations: list[Equality] = [parse_expr(eq, transformations=transformations).simplify() for eq in raw[-1]]
        if len(equations) == 1:
            eq = equations[0]
            parsed[-1] = get_plane(eq)
        elif len(equations) == 2:
            parsed[-1] = get_plane(equations[0]).intersection(get_plane(equations[1]))[0]
        else:
            raise ValueError('Objects defined by more than 2 equations are not supported')
    return list(map(str, parsed))

def process_geometry(raw: str, env: dict) -> tuple[GeometryEntity | None, dict]:
    try:
        parsed, env = safe_eval(construct_string(parse_equations(str_to_list(raw), env)), env)
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
    else:
        return parsed, env