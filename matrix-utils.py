from sympy import Expr, NonSquareMatrixError, Number, ShapeError, init_printing, pprint, nsimplify, factor, solve
from utils import matrix_is_zero, list_to_matrix


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
        if input("Try again? [Y/n] ").lower() == "y":
            producto()
        else:
            exit(1)
    else:
        pprint(factor(nsimplify(result), deep=True))
        

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
        if input("Try again? [Y/n] ").lower() == "y":
            adjunta()
        else:
            exit(1)
    else:
        pprint(factor(nsimplify(result), deep=True))

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
        if input("Try again? [Y/n] ").lower() == "y":
            determinante()
        else:
            exit(1)
    except  ValueError:
        print('ERROR: Mismatched dimensions.')
        if input("Try again? [Y/n] ").lower() == "y":
            determinante()
        else:
            exit(1)
    else:
        pprint(factor(nsimplify(result), deep=True))

def inversa():
    print("INVERSA")
    print("Los elementos de la matriz deben separarse por / y cada fila con //")
    message = [m.split('/') for m in input("Introduce la matriz: ").split('//')] # Split string input into 2D array
    A = list_to_matrix(message)
    print("Resultado:\n")
    try:
        result = A.inv()
    except NonSquareMatrixError:
        print("ERROR: Given matrix not square, thus not invertible")
        if input("Try again? [Y/n] ").lower() == "y":
            inversa()
        else:
            exit(1)
    except ValueError:
        print("ERROR: The determinant of the given matrix is 0, thus it cannot be inverted")
        if input("Try again? [Y/n] ").lower() == "y":
            inversa()
        else:
            exit(1)
    else:
        pprint(factor(nsimplify(result), deep=True))

def rango():
    print("RANGO")
    print("Los elementos de la matriz deben separarse por / y cada fila con //")
    message:list[list[str]] = [m.split('/') for m in input("Introduce la matriz: ").split('//')] # Split string input into 2D array
    A = list_to_matrix(message)
    if A.is_symbolic():
        shape = A.shape
        minors_list: list[Expr] = []
        for row in range(shape[0]):
            for col in range(shape[1]):
                rowlist = list(range(shape[0]))
                collist = list(range(shape[1]))
                if shape[0] > shape[1]:
                    rowlist.remove(row)
                elif shape[1] > shape[0]:
                    collist.remove(col)
                else:
                    rowlist.remove(row)
                    collist.remove(col)
                minors_list.append(factor(nsimplify(A.extract(rowlist, collist).det())))
        zero_values: list[Number] = []
        for minor in minors_list:
            if not minor.is_number:
                for root in solve(minor):
                    if not root in zero_values:
                        zero_values.append(root)
        symbol = sorted(A.free_symbols)[0]
        try:
            print(f"Caso 1, si {str([f'{symbol} ≠ {x}' for x in zero_values]).removeprefix('[\'').removesuffix('\']')}: \n Rango de A = {A.rank()}")
        except ValueError:
            print('ERROR: Mismatched dimensions.')
            if input("Try again? [Y/n] ").lower() == "y":
                rango()
            else:
                exit(1)
        caso = 2
        for root in zero_values:
            try:
                print(f"Caso {caso} si {symbol} = {root}:")
                print(f"Rango de A = {A.subs(symbol, root).rank(simplify=True)}")
            except ValueError:
                print('ERROR: Mismatched dimensions.')
                if input("Try again? [Y/n] ").lower() == "y":
                    rango()
                else:
                    exit(1)
            caso += 1
    else:
        try:
            print(f"El rango de A = {A.rank(iszerofunc=matrix_is_zero)}")
        except ValueError:
            print('ERROR: Mismatched dimensions.')
            if input("Try again? [Y/n] ").lower() == "y":
                rango()
            else:
                exit(1)
        


init_printing()
print("""
    __  __           _            _        
   |  \\/  |   __ _  | |_   _ __  (_) __  __
   | |\\/| |  / _` | | __| | '__| | | \\ \\/ /
   | |  | | | (_| | | |_  | |    | |  >  < 
   |_|  |_|  \\__,_|  \\__| |_|    |_| /_/\\_\\
                                    
    """)
while True:
    option = input("Elige una opción: Adjunta [a], Determinante [d], Producto [p], Inversa [i], Rango [r] o Salir [q]: ")
    if option == "d":
        try:
            determinante()
        except KeyboardInterrupt:
            print()
            continue
    elif option == "a":
        try:
            adjunta()
        except KeyboardInterrupt:
            print()
            continue
    elif option == "p":
        try:
            producto()
        except KeyboardInterrupt:
            print()
            continue
    elif option == "i":
        try:
            inversa()
        except KeyboardInterrupt:
            print()
            continue
    elif option == "r":
        try:
            rango()
        except KeyboardInterrupt:
            print()
            continue
    elif option == "q":
        print("Saliendo...")
        exit(0)