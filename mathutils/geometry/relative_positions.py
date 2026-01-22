from sympy import Eq, Line, Matrix, Plane, Point

from mathutils.matrices.operations import rank


def relpos(*geom):
    if all(isinstance(x, Point) for x in geom):
        return puntos(*geom)
    elif all(isinstance(x, Line) for x in geom):
        if len(geom) != 2:
            raise ValueError('Only relative position of 2 lines is allowed')
        else:
            return rectas(*geom)
    elif all(isinstance(x, Plane) for x in geom):
        if len(geom) <= 3:
            return planos(*geom)
        else:
            raise ValueError("It's only possible to calculate the relative position of up to 3 planes")
    elif len(geom) == 2 and any(isinstance(x, Line) for x in geom) and any(isinstance(x, Plane) for x in geom):
        return recta_plano(next(x for x in geom if isinstance(x, Line)), next(x for x in geom if isinstance(x, Plane)),)



def puntos(*points) -> str:
    if Point.is_collinear(*points):
        return 'alineados'
    elif Point.are_coplanar(*points):
        return 'coplanarios'
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

def planos(p1: Plane, p2: Plane, p3: Plane | None = None):
    if p3 is None:
        if p1.are_concurrent(p2):
            return 'coincidentes'
        elif p1.is_parallel(p2):
            return 'paralelos'
        else:
            return 'secantes'
    else:
        A = Matrix([list(p.normal_vector) for p in [p1,p2,p3]]) # type: ignore
        AB = Matrix([list(p.normal_vector)] + [Eq(p.equation(),0).simplify().rhs] for p in [p1,p2,p3]) # type: ignore
        rgA = rank(A)
        rgAB = rank(AB)
        if isinstance(rgA, int) and isinstance(rgAB, int):
            if rgA == rgAB:
                if rgA == 1:
                    return 'coincidentes'
                elif rgA == 2:
                    concurrencies = [p1.are_concurrent(p2),p1.are_concurrent(p3),p2.are_concurrent(p3)]
                    if any(concurrencies):
                        return '2 coincidentes y uno secante'
                    else:
                        return 'todos secantes en una recta'
                elif rgA == 3:
                    return 'todos secantes en un punto (S.C.D)'
            else:
                if rgA == 1 and rgAB == 2:
                    concurrencies = [p1.are_concurrent(p2),p1.are_concurrent(p3),p2.are_concurrent(p3)]
                    if any(concurrencies):
                        return '2 coincidentes y uno paralelo'
                    else:
                        return '3 paralelos entre sí'
                elif rgA == 2 and rgAB == 3:
                    parallels = [p1.is_parallel(p2),p1.is_parallel(p3),p2.is_parallel(p3)]
                    if any(parallels):
                        return '2 paralelos y uno secante'
                    else:
                        return '3 planos secantes 2 a 2'
        else:
            raise NotImplementedError('Only complete equations with no symbols are allowed')
