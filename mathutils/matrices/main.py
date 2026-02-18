import re

from sympy import NonSquareMatrixError, factor, nsimplify, pprint

from mathutils.parser import safe_eval
from .codec import Main
from .determinants import del_proportional_lines, del_zero_lines
from .rank import print_rank, rank
from .utils import MATRIX_PATTERN, Matrix, matrix_is_zero, parse_matrix


def matrices():
    env = {"classes": [Matrix], "vars": {}, "whitelist": []}
    print("""
    __  __           _            _        
    |  \\/  |   __ _  | |_   _ __  (_) __  __
    | |\\/| |  / _` | | __| | '__| | | \\ \\/ /
    | |  | | | (_| | | |_  | |    | |  >  < 
    |_|  |_|  \\__,_|  \\__| |_|    |_| /_/\\_\\                                        
    """)
    while True:
        raw = input(">> ")
        if raw.replace(" ", "") == "":
            pass
        elif raw.replace(" ","") == "q":
            return
        elif raw.replace(" ","") == "codec":
            Main().app()
        elif re.match(rf"adj (({MATRIX_PATTERN})|\w+)", raw):
            A = get_matrix(raw, 'adj ', env)
            if A:
                try:
                    adjugate = A.adjugate()
                except NonSquareMatrixError:
                    print("ERROR: Given matrix not square, thus ∄ adj A.")
                else:
                    print()
                    pprint(factor(nsimplify(adjugate)))
        elif re.match(rf"det (({MATRIX_PATTERN})|\w+)", raw) or re.match(rf"\|(({MATRIX_PATTERN})|\w+)\|", raw):
            A = get_matrix(raw, ['det ', '|'], env)
            if A:
                try:
                    determinant = A.det(iszerofunc=matrix_is_zero)
                except NonSquareMatrixError:
                    print("ERROR: Given matrix not square, thus ∄ det A.")
                else:
                    pprint(factor(nsimplify(determinant)))
        elif re.match(rf"(rg|rango|rank) (({MATRIX_PATTERN})|\w+)", raw):
            A = get_matrix(raw, ['rg ','rango ','rank '], env)
            if A:
                A = del_proportional_lines(del_zero_lines(A))
                try:
                    ranks = rank(A)
                    print_rank(ranks)
                except ValueError:
                    print("ERROR: Mismatched dimensions.")
        else:
            parsed = re.sub(MATRIX_PATTERN, str(parse_matrix(raw)), raw).replace("^","**")
            try:
                result, env = safe_eval(parsed, env)
            except (ValueError, NameError, TypeError, SyntaxError) as e:
                print(f"ERROR: {e}")
            else:
                if result:
                    print()
                    pprint(result)

def get_matrix(raw: str, op: str | list[str], env: dict) -> Matrix:
    if isinstance(op, list):
        processed = raw
        for o in op:
            processed = processed.replace(o, "")
    else:
        processed = raw.replace(op, "")
    if processed in env["vars"]:
        return env["vars"][processed]
    else:
        matrix = parse_matrix(raw)
        if not matrix:
            raise NameError("Matrix could not be found in stored variables nor parsed.")
        else:
            return matrix