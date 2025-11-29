from sympy import init_printing
from .matrices.main import matrices
from .geometry.main import main as geometry

init_printing()
option = input('Elige un campo. Geometría [g], Matrices [m] o Salir [q]: ')
match option:
    case "g": geometry()
    case "m": matrices()
    case "q": exit(0)