from rich.console import Console

console = Console()



def pattern_T_inverse(n, color='white'):
    """
    Рисует перевернутый прямоугольный треугольник из *
    Parameters
    ----------
    n - (int) число строк
    color = (str) - цвет (по умолчанию белый)

    Returns None
    -------

    """
    color_on = '[bold ' + color + ']'

    spaces = (n - 1) * 2
    for i in range(0, n):
        for j in range(0, spaces):
            console.print(' ', end='')
        for j in range(0, i + 1):
            console.print(color_on + '* ',
                          end='')
        spaces -= 2
        console.print('')


# проверяем

if __name__ == '__main__':
    pattern_T_inverse(6)
    console.print()
    pattern_T_inverse(7, 'yellow')