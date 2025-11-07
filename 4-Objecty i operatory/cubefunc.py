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
    return 2 * (diag ** 2)


# Задание №9
# Три металлических куба с ребрами длиной 3, 4 и 5 см соответственно пере-
# плавляются в один куб. Найдите длину ребра нового куба.

def new_cube(c1, c2, c3):
    """
    Вычисляем длину ребра нового куба, если даны длины рёбер трёх исходных кубов
    Parameters
    ----------
    c1 - длина ребра 1-го куба
    c2 - длина ребра 2-го куба
    c3 - длина ребра 3-го куба

    Returns
    -------

    длина ребра нового куба

    """

    V_all = (c1 ** 3) + (c2 ** 3) + (c3 ** 3)

    return math.ceil(V_all ** (1/3))
