from .vectors import main as vectors


def main():
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

if __name__ == '__main__':
    main()