import numpy as np

def producto():
    print("Los elementos de la matriz deben separarse por / y cada fila con //")
    matrix1 = np.matrix(input("Introduce la primera matriz: ").replace("//", ";").replace("/", ","), dtype=np.int64)
    matrix2 = np.matrix(input("Introduce la segunda matriz: ").replace("//", ";").replace("/", ","), dtype=np.int64)
    print("Resultado:")
    print(np.matmul(matrix1, matrix2))

def adjunta():
    print("Los elementos de la matriz deben separarse por / y cada fila con //")
    matrix = np.matrix(input("Introduce la matriz: ").replace("//", ";").replace("/", ","), dtype=np.int64)
    print("Resultado:")
    print((matrix.I * round(np.linalg.det(matrix))).T.round())

def determinante():
    print("Los elementos de la matriz deben separarse por / y cada fila con //")
    matrix = np.matrix(input("Introduce la matriz: ").replace("//", ";").replace("/", ","), dtype=np.int64)
    print("Resultado:")
    print(round(np.linalg.det(matrix)))

print("""
    __  __           _            _        
   |  \\/  |   __ _  | |_   _ __  (_) __  __
   | |\\/| |  / _` | | __| | '__| | | \\ \\/ /
   | |  | | | (_| | | |_  | |    | |  >  < 
   |_|  |_|  \\__,_|  \\__| |_|    |_| /_/\\_\\
                                    
    """)
while True:
    option = input("Elige una opción: Adjunta [a], Determinante [d], Producto [p] o Salir [q]: ")
    if option == "d":
        determinante()
    elif option == "a":
        adjunta()
    elif option == "p":
        producto()
    elif option == "q":
        print("Saliendo...")
        exit(0)