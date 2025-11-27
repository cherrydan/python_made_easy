"""
Илюстрируем применение обязательных и необязательных именованых аргументов
"""

from rich.console import Console

console = Console()


def parrot(volt, state='мертв', act='оживёт', type='"Норвежский голубой"'):
    """

    Parameters
    ----------
    volt - обязательный
    state - необязательный по умолчанию
    act - необязательный по умолчанию
    type - необязательный по умолчанию

    Returns
    -------
    """

    console.print('[bold yellow]- Этот попугай не ' + act + ',[/bold yellow]', end=' ')
    console.print('[bold red]даже если пропустить ' + str(volt) + ' вольт через него' + '[/bold red]')
    console.print('[bold blue]- Какое оперение? ' + type + '![/bold blue]')
    console.print('[bold white]- Он ' + state + '!'+ '[/bold white]')



if __name__ == '__main__':
    parrot(10000)
    parrot(volt=1000)
    parrot(volt=10000, act='полетит')
    parrot('миллион', 'прыгнет', 'отправится к праотцам')
    parrot('тысячу', 'летает с ангелами', type='Какаду')
    # parrot(volt=5.0, 'скончался') # и тут будет ошибка
    # parrot(5.0, volt=5.0) # тут будет ошибка выполнения
    # parrot(actor='Джон Киз') # и тут будет ошибка





