from rich.console import Console

console = Console()


def pattern_RT_down(n, color='white', spaces=10):
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
    for row in range(n -1, -1, -1):
        # Вычисляем количество пробелов для текущей строки
        # (n - 1) - это пробелы для первой строки,
        # затем уменьшается на 1 для каждой следующей строки
        spaces_to_print = n + spaces - 1 - row
        for _ in range(spaces_to_print):
            console.print(' ', end=' ')

        # Печатаем звёзды
        for _ in range(0, row + 1):
            console.print(color_on + '*  ', end='')

        # Переходим на новую строку только после того, как вся строка напечатана
        console.print()  # Автоматически добавляет новую строку


pattern_RT_down(6, color='red')

