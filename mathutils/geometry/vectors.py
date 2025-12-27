from sympy import Expr
from sympy.vector import CoordSys3D, VectorAdd

from mathutils.parser import construct_string, are_elements_numbers, safe_eval


def str_to_list(raw: str) -> list[str | list]:
    stack: list[list[str | list]] = [[]]
    current = stack[-1]

    for char in raw:
        if char == '(':
            new_list: list[str] = []
            current.append(new_list)
            stack.append(new_list)
            current = new_list

        elif char == ')':
            stack.pop()
            current = stack[-1]
        else:
            if char.isdigit() and current and current[-1] == '-':
                current[-1] = f'-{char}'
            elif char == ',': pass
            else:
                current.append(char)
    return stack[0]

def parse_vectors(lst: list[str | list]) -> list[str | list]:
    parsed = lst.copy()
    for element in lst:
        if type(element) is list:
            if all(isinstance(x,str) for x in element) and len(element) == 3 and are_elements_numbers(element):
                parsed[lst.index(element)] = f'({element[0]}*C.i+{element[1]}*C.j+{element[2]}*C.k)'.replace('+-','-')
            else:
                parsed[lst.index(element)] = parse_vectors(element)
        else:
            match element:
                case '·':
                    index = lst.index(element)
                    parsed[index] = '.dot('
                    parsed.insert(index+2, ')')
                case '^':
                    index = lst.index(element)
                    parsed[index] = '.cross('
                    parsed.insert(index+2, ')')
    return parsed

def process_vectors(raw: str, C: CoordSys3D, env: dict) -> tuple[VectorAdd | Expr | None, dict]:
    try:
        parsed, env = safe_eval(construct_string(parse_vectors(str_to_list(raw))), env)
    except SyntaxError as e:
        print('Input not understood! Look for any formatting or other mistakes and try again.')
        msg_list=list(e.text)
        msg_list.insert(e.offset-1,' ')
        msg_list.insert(e.end_offset+1, ' ')
        print(f'The error was here: {"".join(msg_list)}')
        return None, env
    except TypeError:
        print('Types mismatched! It seems like you are trying to operate a number with a vector in an incompatible way')
        print('Make sure you are doing the correct operations and try again.')
        return None, env
    except ValueError as e:
        print(e)
        return None, env
    except NameError as e:
        print(e)
    else:
        return parsed, env