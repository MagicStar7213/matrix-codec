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