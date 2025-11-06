import math


def cube_capacity(diag):
    """
    Вычисляет объём куба

    Parameters
    ----------
    diag - int/float (диагональ куба)

    Returns - int/float (объём куба в куб. см.)
    -------

    tests - testcube.py

    """
    return (diag ** 3) // (3 * math.sqrt(3))


def cube_square(diag):
    """
    Вычисляет площадь куба

    Parameters
    ----------
    diag - int/float (диагональ куба)

    Returns

    int/float (площадь куба в кв. см)

    -------
    tests - testcube.py

    """
    return 2 * (diag**2)