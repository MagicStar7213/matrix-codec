from sympy.vector import CoordSys3D, BaseVector, VectorAdd, VectorMul
from .vectors import process_vectors


def vectors():
    C = CoordSys3D('C')
    env = { 'class': VectorAdd,
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

def main():
    print("""
    ____                                _                
    / ___|  ___   ___   _ __ ___    ___ | |_  _ __  _   _ 
    | |  _  / _ \\ / _ \\ | '_ ` _ \\  / _ \\| __|| '__|| | | |
    | |_| ||  __/| (_) || | | | | ||  __/| |_ | |   | |_| |
    \\____| \\___| \\___/ |_| |_| |_| \\___| \\__||_|    \\__, |
                                                    |___/ 
    """)
    while True:
        option = input("Elige una opción: Geometría [g], Vectores [v] o Salir [q]: ")
        match option:
            case "g": pass
            case "v": vectors()
            case "q": break
            case _:
                print('Error! Opción no disponible. Vuelve a intentarlo.')
                continue

if __name__ == '__main__':
    main()