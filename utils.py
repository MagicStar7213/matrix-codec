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
    result = []
    for row in matrix:
        new_row = []
        for x in row:
            try:
                x = int(x) if float(x).is_integer() else float(x)
            except ValueError:
                x = parse_expr(x, transformations='all')
            finally:
                new_row.append(x)
        result.append(new_row)
    return Matrix(result)
