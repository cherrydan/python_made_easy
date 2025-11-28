from rich.console import Console

console = Console()


def inclusive_range(*args):
    """

    Parameters
    ----------
    n - top of range

    Returns - list of generated values
    -------

    """


    numargs = len(args)

    start = 0
    step = 1

    if numargs < 1:
        raise TypeError('Expected at lest one argument, got {} '.format(numargs))

    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args

    elif numargs == 3:
        (start, stop, step) = args

    else:
        raise TypeError('Expected at most 3 arguments, got {} '.format(numargs))

    # сам генератор
    i = start

    while i <= stop:
        yield i
        i += step


# проверяем

if __name__ == '__main__':
    n = int(input('Введите ограничительное число '))

    console.print(f'[bold green]Весь диапазон от 0 до {n}[/bold green]')

    for i in inclusive_range(n):
        print(i, end=' ')
    print()

    console.print(f'[bold yellow]Только чётные от 0 до {n}[/bold yellow]')

    for i in inclusive_range(0, n):
        if i % 2 == 0:
            print(i, end=' ')
        else:
            continue

    print()

    console.print(f'[bold blue]Только нечётные от 0 до {n} с шагом 3[/bold blue]')

    for i in inclusive_range(0, n, 3):
        if i % 2 != 0:
            print(i, end=' ')
        else:
            continue

    print()

