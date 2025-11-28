from sympy import Matrix, parse_expr, pretty
from sympy.vector import CoordSys3D, Vector, matrix_to_vector

def scalar():
    print('PRODUCTO ESCALAR')
    C = CoordSys3D('C')
    v1: Vector = matrix_to_vector(Matrix([parse_expr(x, transformations='all') for x in input('Introduce el primer vector: ').split(',')]),C)
    v2: Vector = matrix_to_vector(Matrix([parse_expr(x, transformations='all') for x in input('Introduce el segundo vector: ').split(',')]), C)
    print(f'u\u2192 · v\u2192 = {pretty(v1.dot(v2))}')

def vectorial():
    print('PRODUCTO VECTORIAL')
    C = CoordSys3D('C')
    v1: Vector = matrix_to_vector(Matrix([parse_expr(x, transformations='all') for x in input('Introduce el primer vector: ').split(',')]),C)
    v2: Vector = matrix_to_vector(Matrix([parse_expr(x, transformations='all') for x in input('Introduce el segundo vector: ').split(',')]), C)
    print(f'u\u2192 \u2227 v\u2192 = {pretty(v1.cross(v2))}')

def mix():
    print('PRODUCTO MIXTO')
    C = CoordSys3D('C')
    v1: Vector = matrix_to_vector(Matrix([parse_expr(x, transformations='all') for x in input('Introduce el primer vector: ').split(',')]),C)
    v2: Vector = matrix_to_vector(Matrix([parse_expr(x, transformations='all') for x in input('Introduce el segundo vector: ').split(',')]), C)
    v3: Vector = matrix_to_vector(Matrix([parse_expr(x, transformations='all') for x in input('Introduce el tercer vector: ').split(',')]),C)
    print(f'[u\u2192, v\u2192, w\u2192] = {pretty(v1.dot(v2.cross(v3)))}')