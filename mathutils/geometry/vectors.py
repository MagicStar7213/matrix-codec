from sympy import Expr, Matrix, symbols

from mathutils.parser import construct_string, are_elements_numbers, safe_eval


class Vector():
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __add__(self, other: 'Vector'):
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)
    
    def __sub__(self, other: 'Vector'):
        return self + (-other)
    
    def __mul__(self, other: 'Vector'):
        return self.escalar(other)
    
    def __rmul__(self, other):
        return Vector(other*self.x, other*self.y, other*self.z)
    
    def __xor__(self, other: 'Vector'):
        return self.vectorial(other)

    def escalar(self, v: 'Vector'):
        return self.x*v.x + self.y*v.y + self.z*v.z
    
    def vectorial(self, v:'Vector'):
        i,j,k = symbols('i j k')
        vec = Matrix([[i,j,k],[self.x,self.y,self.z],[v.x,v.y,v.z]]).det()
        return Vector(vec.coeff(i), vec.coeff(j), vec.coeff(k))
    
    def mixto(self, v:'Vector', w: 'Vector'):
        return self.escalar(v.vectorial(w))



def main():
    env = { 'classes': [Vector],
            'whitelist': [],
            'vars': {}}
    print("""
     _   _ _|_  _  ._  _ 
 \\/ (/_ (_  |  (_) |  _\\ """)
    while True:
        raw = input('>> ')
        if raw == 'q':
            return
        else:
            result, env = process_vectors(raw, env)
            if result is not None:
                if isinstance(result,(Vector)):
                    print(f'({result.x},{result.y},{result.z})')
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
                parsed[index] = f'Vector({element[0]},{element[1]},{element[2]})'.replace('+-','-')
            else:
                parsed[index] = parse_vectors(element)
        elif element == '·' or element == '\u2022':
            parsed[index] = '*'
    return parsed

def process_vectors(raw: str, env: dict) -> tuple[Vector | Expr | None, dict]:
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
    parsed, env = safe_eval(construct_string(parse_vectors(str_to_list(raw))), env)
    return parsed, env