from rich.console import Console

console = Console()


def patternB(row, color="white"):
    """
    Рисует что-то похожее на кнопку
    Parameters
    ----------
    row (int) количество рядов
    color (str) цвет

    Returns None
    -------

    """
    color_on = '[bold ' + color + ']'
    peak = row // 2 + 1  # находим середину фигуры

    for i in range(0, peak):
        for j in range(0, i):
            console.print(color_on + '* ', end='')
        console.print('')

    for i in range(peak, 0, -1):
        for j in range(0, i):
            console.print(color_on + '* ', end='')
        console.print('')


if __name__ == '__main__':
    patternB(6)
    patternB(10, 'cyan')
