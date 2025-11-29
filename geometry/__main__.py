from .vectors import scalar, vectorial, mix


def vectors():
    print("""
     _   _ _|_  _  ._  _ 
 \\/ (/_ (_  |  (_) |  _\\ """)
    while True:
        option = input("Elige una opción: Producto escalar [s], Producto vectorial [v], Producto mixto [m] o Salir [q]: ")
        match option:
            case "s": scalar()
            case "v": vectorial()
            case "m": mix()
            case "q": return
            case _:
                print('Error! Opción no disponible. Vuelve a intentarlo.')
                continue

print("""
   ____                                _                
  / ___|  ___   ___   _ __ ___    ___ | |_  _ __  _   _ 
 | |  _  / _ \\ / _ \\ | '_ ` _ \\  / _ \\| __|| '__|| | | |
 | |_| ||  __/| (_) || | | | | ||  __/| |_ | |   | |_| |
  \\____| \\___| \\___/ |_| |_| |_| \\___| \\__||_|    \\__, |
                                                  |___/ 
""")
while True:
    option = input("Elige una opción: Geometría [g], Vectores [v] o Salir [q]: ")
    match option:
        case "g": pass
        case "v": vectors()
        case "q": break
        case _:
            print('Error! Opción no disponible. Vuelve a intentarlo.')
            continue