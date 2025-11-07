from sympy import Expr, Matrix, NonSquareMatrixError, Number, ShapeError, init_printing, parse_expr, pprint, nsimplify, factor, solve
from determinants import del_proportional_lines, del_zero_lines
from utils import matrix_is_zero, list_to_matrix, decompose_matrix


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
    A = del_proportional_lines(del_zero_lines(list_to_matrix(message)))
    if A.is_symbolic():
        if A.shape[0] != A.shape[1]:
            minors_list: list[Matrix] = decompose_matrix([A])
            all_square = True
            for minor in minors_list:
                    if minor.shape[0] != minor.shape[1]:
                        all_square = False
            while not all_square:
                all_square = True
                for minor in minors_list:
                    if minor.shape[0] != minor.shape[1]:
                        all_square = False
                        break
                if not all_square:
                    minors_list = decompose_matrix(minors_list)
            zero_values: list[Number] = []
            for raw_minor in minors_list:
                minor = del_proportional_lines(del_zero_lines(raw_minor))
                if not minor.det().is_number:
                    for root in solve(minor.det()):
                        sym = list(minor.free_symbols)[0]
                        minors_affected = 1
                        mins = minors_list.copy()
                        mins.remove(minor)
                        for m in mins:
                            if m.subs(sym, root).det() == 0:
                                minors_affected += 1
                        if minors_affected == len(minors_list) and not root in zero_values:
                            zero_values.append(root)
            symbol = sorted(A.free_symbols)[0]
            if len(zero_values) != 0:
                try:
                    str1 = "[\'"
                    str2 = "\']"
                    print(f"Caso 1, si {str([f'{symbol} ≠ {x}' for x in zero_values]).removeprefix(str1).removesuffix(str2)}: \n Rango de A = {A.rank()}")
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
                        print(f" Rango de A = {A.subs(symbol, root).rank(simplify=True)}")
                    except ValueError:
                        print('ERROR: Mismatched dimensions.')
                        if input("Try again? [Y/n] ").lower() == "y":
                            rango()
                        else:
                            exit(1)
                    caso += 1
        else:
            try:
                print(f"El rango de A = {A.rank()}")
            except ValueError:
                print('ERROR: Mismatched dimensions.')
                if input("Try again? [Y/n] ").lower() == "y":
                    rango()
                else:
                    exit(1) 
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