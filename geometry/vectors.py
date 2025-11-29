from sympy import Matrix, parse_expr, pretty
from sympy.vector import CoordSys3D, Vector, matrix_to_vector

def scalar():
    print('PRODUCTO ESCALAR')
    C = CoordSys3D('C')
    u: Vector = matrix_to_vector(Matrix([parse_expr(x, transformations='all') for x in input('Introduce el primer vector: ').split(',')]),C)
    v: Vector = matrix_to_vector(Matrix([parse_expr(x, transformations='all') for x in input('Introduce el segundo vector: ').split(',')]), C)
    print(f'u\u2192 · v\u2192 = {pretty(u.dot(v))}')

def vectorial():
    print('PRODUCTO VECTORIAL')
    C = CoordSys3D('C')
    u: Vector = matrix_to_vector(Matrix([parse_expr(x, transformations='all') for x in input('Introduce el primer vector: ').split(',')]),C)
    v: Vector = matrix_to_vector(Matrix([parse_expr(x, transformations='all') for x in input('Introduce el segundo vector: ').split(',')]), C)
    u_v = u.cross(v).to_matrix(C)
    print(f'u\u2192 \u2227 v\u2192 = ({u_v[0]}, {u_v[1]}, {u_v[2]})')

def mix():
    print('PRODUCTO MIXTO')
    C = CoordSys3D('C')
    u: Vector = matrix_to_vector(Matrix([parse_expr(x, transformations='all') for x in input('Introduce el primer vector: ').split(',')]),C)
    v: Vector = matrix_to_vector(Matrix([parse_expr(x, transformations='all') for x in input('Introduce el segundo vector: ').split(',')]), C)
    w: Vector = matrix_to_vector(Matrix([parse_expr(x, transformations='all') for x in input('Introduce el tercer vector: ').split(',')]),C)
    print(f'[u\u2192, v\u2192, w\u2192] = {pretty(u.dot(v.cross(w)))}')