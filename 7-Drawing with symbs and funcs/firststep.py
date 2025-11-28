from rich.console import Console

console = Console()


def patternT(n, color='white'):
    """

    Parameters
    ----------
    n - (int) высота треугольника (строк)
    color - (str) цвет (по умолчанию белый)

    Returns None
    -------
    """
    color_on = '[bold ' + color + ']'
    color_off = '[/bold ' + color + ']'
    # console.print(color_on)
    for row in range(0, n):
        for stars in range(0, row + 1):
            console.print(color_on + '* ', end='')
        console.print('')

    # console.print(color_off)


# проверяем

if __name__ == '__main__':
    patternT(6)
    print()
    patternT(4, 'red')
