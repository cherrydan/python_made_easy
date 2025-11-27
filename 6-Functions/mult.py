"""

Напишем тестовую функцию с переменным числом аргументов
"""


def mult(*args):
    """
    Функция с переменным числом аргументов перемножает аргументы
    Parameters
    ----------
    args - числа

    Returns-результат перемножения аргументов
    -------

    """
    list_args = []
    list_args = list(args)
    val = 1
    for arg in list_args:
        val *= arg
    return val


if __name__ == '__main__':
    print(mult(1, 2, 3, 4, 5))
