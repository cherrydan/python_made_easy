"""
Расчитывает минимальный срок службы машины,
 при котором инвестирование в неё будет более привлекательным,
 по сравнению с инвестициями в другие виды

 сделано при помощи ИИ, зато я в таблицу красивую оформил
"""
from rich.console import Console
from rich.table import Table

console = Console()


def calculate_car_advantage(annual_income: float, init_cost: float,
                            salvage_val: float, alt_rate: float):
    """

    Parameters
    ----------
    annual_income - годовой доход
    init_cost - начальная стоимость
    salvage_val - продажа при утилизации
    alt_rate - альтернативные вложения

    Returns
    -------
    int: количество лет срока службы

    """
    console.print(f"[bold green]Годовой доход от машины {annual_income} руб.[/bold green]")
    console.print(f"[bold yellow]Цена покупки машины {init_cost} руб. [/bold yellow]")
    console.print(f"[bold red]Ликвидационная стоимость машины {salvage_val} руб.[/bold red]")
    console.print(f"[bold yellow]Ставка альтернативных инвестиций {alt_rate}% [/bold yellow]")

    table = Table(title="Автомобиль как инвестиция")
    table.add_column(header="Год", style="cyan", no_wrap=True)
    table.add_column(header="Доход от авто", justify="center")
    table.add_column(header="Доход от альт.", justify="center")
    table.add_column(header="Авто привлекат?", justify="left", style="red")

    n = 0  # срок службы в годах

    while True:
        n += 1
        # Доход от машины = (годовой доход * количество лет) + ликвидационная стоимость
        machine_total_value = (annual_income * n) + salvage_val

        # Доход от альтернативных инвестиций = начальная стоимость * (1 + ставка)^N
        alternative_total_value = float(format((init_cost * ((1 + alt_rate) ** n)), '.2f'))

        row_style = "yellow"
        is_machine_more_attractive = "Нет"
        if machine_total_value > alternative_total_value:
            row_style = "red"
            is_machine_more_attractive = "Да"

        table.add_row(str(n), str(machine_total_value), str(alternative_total_value),
                      str(is_machine_more_attractive),
                      style=row_style)

        if machine_total_value > alternative_total_value:
            console.print(table)
            return n


if __name__ == '__main__':
    # Данные задачи
    annual_income_val = 200000
    initial_cost_val = 1000000
    salvage_value_val = 250000
    alternative_rate_val = 0.08
    min_service_life = calculate_car_advantage(annual_income_val, initial_cost_val, salvage_value_val,
                                               alternative_rate_val)
    console.print(f"[bold red]\nМинимальный срок службы машины, при котором она станет более привлекательной: "
                  f"{min_service_life} лет.[/bold red]")

