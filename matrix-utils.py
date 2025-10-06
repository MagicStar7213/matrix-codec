from sympy import NonSquareMatrixError, init_printing, Matrix, pprint, nsimplify
from utils import list_is_ints, matrix_is_zero


def producto():
    print("PRODUCTO")
    print("Los elementos de la matriz deben separarse por / y cada fila con //")
    message1 = [m.split('/') for m in input("Introduce la primera matriz: ").split('//')] # Split string input into 2D array
    message2 = [m.split('/') for m in input("Introduce la segunda matriz: ").split('//')]
    A = Matrix([list(map(int if list_is_ints(i) else float, i)) for i in message1]) # Convert all elements of matrix to float
    B = Matrix([list(map(int if list_is_ints(i) else float, i)) for i in message2])
    print("Resultado:\n")
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

def inversa():
    print("INVERSA")
    print("Los elementos de la matriz deben separarse por / y cada fila con //")
    message = [m.split('/') for m in input("Introduce la matriz: ").split('//')] # Split string input into 2D array
    A = Matrix([list(map(int if list_is_ints(i) else float, i)) for i in message]) # Convert all elements of matrix to float
    print("Resultado:\n")
    try:
        result = (A.inv()).tolist()
    except NonSquareMatrixError:
        print("ERROR: Given matrix not square, thus not invertible")
        if input("Try again? [Y/n]").lower() == "y":
            inversa()
        else:
            exit(1)
    except ValueError:
        print("ERROR: The determinant of the given matrix is 0, thus it cannot be inverted")
        if input("Try again? [Y/n]").lower() == "y":
            inversa()
        else:
            exit(1)
    else:
        pprint(Matrix([list(map(int if list_is_ints(i) else nsimplify, i)) for i in result]))

init_printing(use_unicode=True)
print("""
    __  __           _            _        
   |  \\/  |   __ _  | |_   _ __  (_) __  __
   | |\\/| |  / _` | | __| | '__| | | \\ \\/ /
   | |  | | | (_| | | |_  | |    | |  >  < 
   |_|  |_|  \\__,_|  \\__| |_|    |_| /_/\\_\\
                                    
    """)
while True:
    option = input("Elige una opción: Adjunta [a], Determinante [d], Producto [p], Inversa [i] o Salir [q]: ")
    if option == "d":
        determinante()
    elif option == "a":
        adjunta()
    elif option == "p":
        producto()
    elif option == "i":
        inversa()
    elif option == "q":
        print("Saliendo...")
        exit(0)