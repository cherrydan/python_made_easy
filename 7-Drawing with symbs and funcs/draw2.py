from rich.console import Console

console = Console()


def patternT(n, color='white'):
    """
    Рисует прямоугольный треугольник из *
    Parameters
    ----------
    n - (int) высота треугольника (строк)
    color - (str) цвет (по умолчанию белый)

    Returns None
    -------
    """
    color_on = '[bold ' + color + ']'

    # console.print(color_on)
    for row in range(0, n):
        for stars in range(0, row + 1):
            console.print(color_on + '*  ', end='')
        console.print('')


def patternT_down(n, color='white'):
    """
    Рисует прямоугольный треугольник из *
    Parameters
    ----------
    n - (int) высота треугольника (строк)
    color - (str) цвет (по умолчанию белый)

    Returns None
    -------
    """
    color_on = '[bold ' + color + ']'

    # console.print(color_on)
    for row in range(n - 1, -1, -1):
        for stars in range(0, row + 1):
            console.print(color_on + '*  ', end='')
        console.print('')


patternT(6)
console.print()
patternT_down(6)
