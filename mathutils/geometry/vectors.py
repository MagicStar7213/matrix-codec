from sympy import Expr
from sympy.vector import CoordSys3D, VectorAdd, BaseVector, VectorMul

from mathutils.parser import construct_string, are_elements_numbers, safe_eval


def main():
    C = CoordSys3D('C')
    env = { 'classes': [BaseVector, VectorAdd, VectorMul],
            'whitelist': ['dot', 'cross'],
            'vars': {'C': C}, 'attrs': ['i', 'j', 'k']}
    print("""
     _   _ _|_  _  ._  _ 
 \\/ (/_ (_  |  (_) |  _\\ """)
    while True:
        raw = input('>> ')
        if raw == 'q':
            return
        else:
            result, env = process_vectors(raw, C, env)
            if result is not None:
                if type(result) in [BaseVector, VectorAdd, VectorMul]:
                    print(f'({result.components[C.i] if C.i in result.components.keys() else 0},{result.components[C.j] if C.j in result.components.keys() else 0},{result.components[C.k] if C.k in result.components.keys() else 0})')
                else:
                    print(result)

def str_to_list(raw: str) -> list[str | list]:
    stack: list[list[str | list]] = [[]]
    current = stack[-1]

    for char in raw:
        if char == '(':
            new_list = []
            current.append(new_list)
            stack.append(new_list)
            current = new_list

        elif char == ')':
            stack.pop()
            current = stack[-1]
        else:
            if char.isdigit() and current and current[-1] == '-':
                current[-1] = f'-{char}'
            elif char == ',':
                pass
            else:
                current.append(char)
    return stack[0]

def parse_vectors(lst: list[str | list]) -> list[str | list]:
    parsed = lst.copy()
    for index, element in enumerate(lst):
        if type(element) is list:
            if all(isinstance(x,str) for x in element) and len(element) == 3 and are_elements_numbers(element):
                parsed[index] = f'({element[0]}*C.i+{element[1]}*C.j+{element[2]}*C.k)'.replace('+-','-')
            else:
                parsed[index] = parse_vectors(element)
        else:
            if element == '·' or element == '\u2022':
                parsed[index] = '.dot('
                parsed.insert(index+2, ')')
            elif element ==  '^':
                parsed[index] = '.cross('
                parsed.insert(index+2, ')')
    return parsed

def process_vectors(raw: str, C: CoordSys3D, env: dict) -> tuple[VectorAdd | Expr | None, dict]:
    try:
        safe_eval(construct_string(parse_vectors(str_to_list(raw))), env)
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
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')
        return None, env
    parsed, env = safe_eval(construct_string(parse_vectors(str_to_list(raw))), env)
    return parsed, env