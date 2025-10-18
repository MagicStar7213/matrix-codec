from sympy import NonSquareMatrixError, ShapeError, init_printing, Matrix, pprint, nsimplify, parse_expr
import sympy
from utils import list_is_ints, matrix_is_zero, list_to_matrix


def producto():
    print("PRODUCTO")
    print("Los elementos de la matriz deben separarse por / y cada fila con //")
    message1 = [m.split('/') for m in input("Introduce la primera matriz: ").split('//')] # Split string input into 2D array
    message2 = [m.split('/') for m in input("Introduce la segunda matriz: ").split('//')]
    A = list_to_matrix(message1)
    B = list_to_matrix(message2)
    print("Resultado:\n")
    try:
        result = A*B
    except ShapeError:
        print(f"ERROR: A ({A.rows}x{A.cols}) is not multipliable with B ({B.rows}x{B.cols})")
        if input("Try again? [Y/n]").lower() == "y":
            producto()
        else:
            exit(1)
    else:
        pprint(result.applyfunc(nsimplify))
        

def adjunta():
    print("ADJUNTA")
    print("Los elementos de la matriz deben separarse por / y cada fila con //")
    message = [m.split('/') for m in input("Introduce la matriz: ").split('//')] # Split string input into 2D array
    A = list_to_matrix(message)
    print("Resultado: \n")
    try:
        result = A.adjugate()
    except NonSquareMatrixError:
        print("ERROR: Given matrix not square, thus there cannot be an adjugate of A.")
        if input("Try again? [Y/n]").lower() == "y":
            adjunta()
        else:
            exit(1)
    else:
        pprint(result.applyfunc(nsimplify))

def determinante():
    print("DETERMINANTE")
    print("Los elementos de la matriz deben separarse por / y cada fila con //")
    message:list[list[str]] = [m.split('/') for m in input("Introduce la matriz: ").split('//')] # Split string input into 2D array
    A = list_to_matrix(message)
    print("Resultado:")
    try:
        result = A.det(iszerofunc=matrix_is_zero)
    except NonSquareMatrixError:
        print("ERROR: Given matrix not square, thus there cannot be a determinant for A.")
        if input("Try again? [Y/n]").lower() == "y":
            determinante()
        else:
            exit(1)
    else:
        pprint(sympy.factor(nsimplify(result)))

def inversa():
    print("INVERSA")
    print("Los elementos de la matriz deben separarse por / y cada fila con //")
    message = [m.split('/') for m in input("Introduce la matriz: ").split('//')] # Split string input into 2D array
    A = list_to_matrix(message)
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
        pprint(sympy.factor(nsimplify(result)))

init_printing()
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