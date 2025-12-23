from sympy.vector import CoordSys3D, VectorAdd


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
                case '·': parsed[lst.index(element)] = '.dot'
                case '^': parsed[lst.index(element)] = '.cross'
    return parsed

def are_elements_numbers(l: list[str]) -> bool:
    for x in l:
        try:
            float(x)
        except ValueError:
            return False
    return True

def construct_string(l: list[str | list]) -> str:
    return ''.join([construct_string(x) if type(x) is list else x for x in l])

def convert_to_vectors(raw: str) -> VectorAdd:
    C = CoordSys3D('C')
    return eval(construct_string(parse_vectors(str_to_list(raw))))