from sympy import init_printing
from .operations import determinante, adjunta, producto, inversa, rango
from .codec import Main


init_printing()
print("""
    __  __           _            _        
   |  \\/  |   __ _  | |_   _ __  (_) __  __
   | |\\/| |  / _` | | __| | '__| | | \\ \\/ /
   | |  | | | (_| | | |_  | |    | |  >  < 
   |_|  |_|  \\__,_|  \\__| |_|    |_| /_/\\_\\
                                    
    """)
while True:
    option = input("Elige una opción: Adjunta [a], Codificador/decodificador [c], Determinante [d], Inversa [i], Producto [p], Rango [r] o Salir [q]: ")
    match option:
        case "d":
            try:
                determinante()
            except KeyboardInterrupt:
                print()
                continue
        case "a":
            try:
                adjunta()
            except KeyboardInterrupt:
                print()
                continue
        case "p":
            try:
                producto()
            except KeyboardInterrupt:
                print()
                continue
        case "i":
            try:
                inversa()
            except KeyboardInterrupt:
                print()
                continue
        case "r":
            try:
                rango()
            except KeyboardInterrupt:
                print()
                continue
        case "q":
            print("Saliendo...")
            exit(0)
        case "c":
            try:
                Main().app()
            except KeyboardInterrupt:
                print()
                continue
        case _:
            print('ERROR: No existe esa opción.')
            continue