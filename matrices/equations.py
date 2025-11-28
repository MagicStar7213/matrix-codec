import sympy


print("ECUACIONES")
print(f"""Esto es una consola para especificar las caracteristicas de un problema completo.
De esta forma, se puede escribir que A = {[[1,0,-2],[0,3,1],[-1,2,0]]} y despejar X en la ecuación A·X=3I, por ejemplo.""")
matrix_separators = ',;:_|\\#/'
while True:
    raw_expr = input('>> ')
    mat_list = [x.split(',') for x in raw_expr.split('=')[1].split(',,')]