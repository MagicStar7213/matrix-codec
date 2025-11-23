import warnings
from sympy import Matrix, parse_expr


def matrix_is_zero(x):
    result = x.is_zero
    if result is None:
        warnings.warn(f"Zero testing of {x} evaluated into None")
    return result

def list_is_ints(lst: list[str]) -> bool:
    for x in lst:
        try:
            float(x)
        except ValueError:
            return False
        else:
            if not float(x).is_integer():
                return False
    return True

def list_to_matrix(matrix: list[list[str]]) -> Matrix:
    return Matrix([[parse_expr(x, transformations='all') for x in row] for row in matrix])

def decompose_matrix(matrix_list: list[Matrix]) -> list[Matrix]:
    return_list: list[Matrix] = []
    for A in matrix_list:
        shape = A.shape
        minors_list: list[Matrix] = []
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
                minor = A.extract(rowlist, collist)
                if minor not in minors_list:
                    minors_list.append(minor)
        return_list.extend(minors_list)
    return return_list