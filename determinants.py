from sympy import Matrix, Expr, LessThan, Rational, factor, nan, gcd, prod


def del_zero_lines(matrix: Matrix) -> Matrix:
    new_matrix = matrix.copy()
    for row in range(matrix.shape[0]):
        if new_matrix.row(row) == Matrix.zeros(1, new_matrix.shape[1]):
            new_matrix.row_del(row)
    for col in range(matrix.shape[1]):
        if new_matrix.col(col) == Matrix.zeros(new_matrix.shape[0],1):
            new_matrix.col_del(col)
    return new_matrix

def del_proportional_lines(matrix: Matrix) -> Matrix:
    new_matrix = matrix.copy()
    del_rows:list[int] = []
    for row in range(matrix.shape[0]):
        if row not in del_rows:
            for row1 in range(matrix.shape[0]):
                if row == row1:
                    pass
                else:
                    k = [Rational(matrix[row,col], matrix[row1,col]) for col in range(matrix.shape[1])]
                    if k.count(nan) != len(k) and k.count(k[0]) == len(k) and row1 not in del_rows:
                        del_rows.append(row1 if LessThan(matrix[row,0], matrix[row1,0]) else row)
    del_rows.reverse()
    for r in del_rows:
        print(f'Trying to remove row {r}')
        new_matrix.row_del(r)
    del_cols:list[int] = []
    for col in range(matrix.shape[1]):

        if col not in del_cols:
            for col1 in range(matrix.shape[1]):
                if col == col1:
                    pass
                else:
                    k = [Rational(matrix[row,col], matrix[row,col1]) for row in range(matrix.shape[0])]
                    if k.count(nan) != len(k) and k.count(k[0]) == len(k) and col1 not in del_cols:
                        del_cols.append(col1 if LessThan(matrix[0,col], matrix[0,col1]) else col)
    del_cols.reverse()
    for c in del_cols:
        print(f'Trying to remove column {c}')
        new_matrix.col_del(c)
    return new_matrix

def extract_common_factor(matrix: Matrix) -> tuple[Expr,Matrix] | Matrix:
    new_matrix = matrix.copy()
    common_factors: list[Expr|Matrix] = []
    for row in range(matrix.shape[0]):
        mcd = gcd([x for x in new_matrix.row(row)])
        if mcd != 1:
            common_factors.append(mcd)
            for col in range(matrix.shape[1]):
                new_matrix[row,col] /= mcd
    for col in range(matrix.shape[1]):
        mcd = gcd([x for x in new_matrix.col(col)])
        if mcd != 1:
            common_factors.append(mcd)
            for row in range(matrix.shape[0]):
                new_matrix[row,col] /= mcd
    return (factor(prod(common_factors)), new_matrix) if common_factors else matrix