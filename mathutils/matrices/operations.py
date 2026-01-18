from sympy import Expr, Integer, Matrix, NonSquareMatrixError, ShapeError, Symbol, ordered, pprint, nsimplify, factor, solve
from .determinants import del_proportional_lines, del_zero_lines
from .utils import matrix_is_zero, list_to_matrix, decompose_matrix


def rank(A: Matrix, minors_list:list[Matrix] | None = None, unequalities: list[Expr] | None = None, symbols: list[Symbol] | None=None) -> list[tuple[tuple[Symbol, Expr | list[Expr]], int | list]] | int:
    if A.is_symbolic():
        if minors_list is None:
            minors_list = []
            if A.shape[0] != A.shape[1]:
                minors_list = decompose_matrix([A])
                while not all(minor.is_square for minor in minors_list):
                    square_minors = [minor for minor in minors_list if minor.is_square]
                    non_square_minors = [minor for minor in minors_list if not minor.is_square]
                    minors_list = decompose_matrix(non_square_minors) + square_minors
            else:
                minors_list = [A]
        if symbols is None:
            symbols = list(ordered(A.free_symbols))
        symbol = symbols[0]
        zero_values: list[Expr] = []
        for raw_minor in minors_list:
            minor = del_proportional_lines(del_zero_lines(raw_minor))
            if not Expr(minor.det()).is_number and symbol in Expr(minor.det()).free_symbols:
                for root in solve(minor.det(), symbol):
                    if all(Matrix(m.subs(symbol, root)).det() == 0 or not Expr(Matrix(m.subs(symbol, root)).det()).is_number for m in [M for M in minors_list if M != minor]) and root not in zero_values:
                        if unequalities is None or root not in unequalities:
                            zero_values.append(root)
        if A.subs(symbol,0).is_zero_matrix and Integer(0) not in zero_values:
            zero_values.append(Integer(0))
        if zero_values:
            ranks: list[tuple[tuple[Symbol, Expr | list[Expr]], int | list]] = []
            new_unequalities = zero_values + (unequalities if unequalities else [])
            syms_new: list[Symbol] = [x for x in symbols if x != symbol]
            ranks.append(((symbol, new_unequalities), rank(A, minors_list, new_unequalities, syms_new) if syms_new else A.rank()))
            for root in zero_values:
                B = Matrix(A.subs(symbol, root))
                syms_new: list[Symbol] = [x for x in symbols if x != symbol]
                ranks.append(((symbol, root), rank(B, [minor.subs(symbol, root) for minor in minors_list], None, syms_new) if syms_new else B.rank()))
            return ranks
        else:
            return A.rank()
    else:
        return A.rank(iszerofunc=matrix_is_zero)


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
    try:
        ranks = rank(A)
        print_rank(ranks)
    except ValueError:
        print("ERROR: Mismatched dimensions.")
        if input("Try again? [Y/n] ").lower() == "y":
            rango()
        else:
            exit(1)

def print_rank(ranks: list[tuple[tuple[Symbol, Expr | list[Expr]], int | list]] | int, indents: int = 0):
    indentation = "".join(["  " for _ in range(indents)])
    pref = "["
    suff = "]"
    if isinstance(ranks, list):
        caso_1 = ranks[0]
        print(f"""{indentation}Caso 1, si {caso_1[0][0]} ≠ {str(caso_1[0][1]).removeprefix(pref).removesuffix(suff).replace("'","")}:""")
        print_rank(caso_1[1],indents+1)
        for caso in ranks[1:]:
            print(f"{indentation}Caso {ranks.index(caso)+1} si {caso[0][0]} = {caso[0][1]}:")
            print_rank(caso[1],indents+1)
    else:
        print(indentation+f'El rango de A = {ranks}')