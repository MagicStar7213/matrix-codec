import re
import warnings
from sympy import MutableDenseMatrix, parse_expr


class Matrix(MutableDenseMatrix):
    pass

MATRIX_PATTERN = r"(\d+x\d+)\((\w+(?: \w+)*)\)"

def parse_matrix(raw: str) -> Matrix | None:
    raw_matrix = re.search(MATRIX_PATTERN, re.sub(r"\s{2,}", " ", raw))
    if raw_matrix:
        try:
            dimensions = tuple(map(int,raw_matrix.group(1).split('x')))
            if not 0 < len(dimensions) < 3:
                raise ValueError('Matrix dimensions introduced are not valid')
        except ValueError as e:
            print(f'Value error: {e}')
            return None
        else:
            if len(dimensions) == 1:
                dimensions += dimensions
            elts = list(map(parse_expr, raw_matrix.group(2).split(" ")))
            return Matrix(*dimensions,elts)

def matrix_is_zero(x):
    result = x.is_zero
    if result is None:
        warnings.warn(f"Zero testing of {x} evaluated into None")
    return result

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