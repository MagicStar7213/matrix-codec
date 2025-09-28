from sympy import init_printing, Matrix, pprint, nsimplify
from utils import list_is_ints, matrix_is_zero


def producto():
    print("PRODUCTO")
    print("Los elementos de la matriz deben separarse por / y cada fila con //")
    message1 = [m.split('/') for m in input("Introduce la primera matriz: ").split('//')] # Split string input into 2D array
    message2 = [m.split('/') for m in input("Introduce la segunda matriz: ").split('//')]
    A = Matrix([list(map(int if list_is_ints(i) else float, i)) for i in message1]) # Convert all elements of matrix to float
    B = Matrix([list(map(int if list_is_ints(i) else float, i)) for i in message2])
    print("Resultado:")
    result = A*B
    pprint(Matrix([list(map(int if list_is_ints(i) else nsimplify, i)) for i in result]))

def adjunta():
    print("ADJUNTA")
    print("Los elementos de la matriz deben separarse por / y cada fila con //")
    message = [m.split('/') for m in input("Introduce la matriz: ").split('//')] # Split string input into 2D array
    A = Matrix([list(map(int if list_is_ints(i) else float, i)) for i in message]) # Convert all elements of matrix to float
    print("Resultado: \n")
    result = A.adjugate().tolist()
    pprint(Matrix([list(map(int if list_is_ints(i) else nsimplify, i)) for i in result]))

def determinante():
    print("DETERMINANTE")
    print("Los elementos de la matriz deben separarse por / y cada fila con //")
    message = [m.split('/') for m in input("Introduce la matriz: ").split('//')] # Split string input into 2D array
    A = Matrix([list(map(int if list_is_ints(i) else float, i)) for i in message]) # Convert all elements of matrix to float
    print("Resultado:")
    result = A.det(iszerofunc=matrix_is_zero)
    pprint(int(result) if float(result).is_integer() else result)

init_printing(use_unicode=True)
print("""
    __  __           _            _        
   |  \\/  |   __ _  | |_   _ __  (_) __  __
   | |\\/| |  / _` | | __| | '__| | | \\ \\/ /
   | |  | | | (_| | | |_  | |    | |  >  < 
   |_|  |_|  \\__,_|  \\__| |_|    |_| /_/\\_\\
                                    
    """)
while True:
    option = input("Elige una opción: Adjunta [a], Determinante [d], Producto [p] o Salir [q]: ")
    if option == "d":
        determinante()
    elif option == "a":
        adjunta()
    elif option == "p":
        producto()
    elif option == "q":
        print("Saliendo...")
        exit(0)