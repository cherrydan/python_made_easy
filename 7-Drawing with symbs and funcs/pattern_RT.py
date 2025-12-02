from rich.console import Console

console = Console()


def pattern_RT(n, color='white'):
    """
    Рисуем равносторонний треугольник (ёлочку)
    Parameters
    ----------
    n (int) количество строк
    color (str) цвет (по умолчанию - белый)

    Returns None
    -------

    """
    color_on = '[bold ' + color + ']'
    for row in range(0, n):
        # Вычисляем количество пробелов для текущей строки
        # (n - 1) - это пробелы для первой строки,
        # затем уменьшается на 1 для каждой следующей строки
        spaces_to_print = n - 1 - row
        for _ in range(spaces_to_print):
            console.print(' ', end='')

        # Печатаем звёзды
        for _ in range(0, row + 1):
            console.print(color_on + '* ', end='')

        # Переходим на новую строку только после того, как вся строка напечатана
        console.print()  # Автоматически добавляет новую строку


pattern_RT(6)
console.print()
pattern_RT(10, 'green')
