from sympy import Line, Plane, Point


def relpos(*geom):
    relation = ''
    if all(isinstance(x, Point) for x in geom):
        relation = puntos(*geom)
    if all(isinstance(x, Line) for x in geom):
        if len(geom) != 2:
            raise ValueError('Only relative position of 2 lines is allowed')
        else:
            relation = rectas(*geom)


def puntos(*points) -> str:
    if Point.are_coplanar(*points):
        return 'coplanarios'
    elif Point.is_collinear(*points):
        return 'alineados'
    else:
        return 'ni alineados ni coplanarios'

def rectas(r1: Line, r2: Line) -> str:
    if Line.are_concurrent(r1,r2):
        return 'coincidentes'
    elif Line.is_parallel(r1,r2):
        return 'paralelas'
    elif r1.intersection(r2):
        return 'secantes'
    else:
        return 'se cruzan'

def recta_plano(r: Line, p: Plane):
    if p.is_coplanar(r):
        return 'coincidentes'
    elif p.is_parallel(r):
        return 'paralelos'
    else:
        return 'secantes'