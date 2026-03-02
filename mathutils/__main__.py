from sympy import init_printing
from .matrices.main import matrices
from .geometry.main import main as geometry

def main():
    init_printing()
    while True:
        option = input('Elige un campo. Geometría [g], Matrices [m] o Salir [q]: ')
        if option == "g":
            geometry()
        elif option == "m":
            matrices()
        elif option == "q":
            exit(0)

main()