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
            console.print(color_on + '* ', end='')
        console.print('')


# проверяем

if __name__ == '__main__':
    patternT(6)
    print()
    patternT(4, 'red')
