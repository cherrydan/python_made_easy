def calculate_selling_price(cost_price, profit_percentage, overhead_percentage):
    """
    Рассчитывает цену продажи товара с учетом прибыли и накладных расходов.

    Аргументы:
        cost_price (float): Цена покупки (себестоимость).
        profit_percentage (float): Процент прибыли от цены покупки (например, 25 для 25%).
        overhead_percentage (float): Процент накладных расходов от цены продажи (например, 5 для 5%).

    Возвращает:
        float: Итоговая цена продажи.
    """

    print(f"Цена покупки: ${cost_price}")
    print(f"Процент прибыли от цены покупки: {profit_percentage}%")
    print(f"Процент накладных расходов от цены продажи: {overhead_percentage}%")

    # Переводим проценты в десятичные дроби
    profit_factor = profit_percentage / 100
    overhead_factor = overhead_percentage / 100

    # 1. Расчет прибыли в денежном выражении
    profit_amount = cost_price * profit_factor
    print(f"\nПрибыль в денежном выражении: ${cost_price} * {profit_factor} = ${profit_amount:.2f}")

    # 2. Расчет базовой цены продажи (себестоимость + прибыль)
    base_selling_price = cost_price + profit_amount
    print(
        f"Базовая цена продажи (без учета накладных расходов): ${cost_price} + ${profit_amount:.2f} = ${base_selling_price:.2f}")

    # 3. Учет накладных расходов (5% от Цены продажи)
    # Пусть P - искомая цена продажи
    # P = base_selling_price + (overhead_factor * P)
    # P - (overhead_factor * P) = base_selling_price
    # P * (1 - overhead_factor) = base_selling_price
    # P = base_selling_price / (1 - overhead_factor)

    # 4. Расчет итоговой цены продажи
    final_selling_price = base_selling_price / (1 - overhead_factor)
    print(f"Расчетная цена продажи P: ${base_selling_price:.2f} / (1 - {overhead_factor}) = ${final_selling_price:.2f}")

    return final_selling_price


# Данные для задачи
cost = 1800
profit_pc = 25
overhead_pc = 5

# Вызов функции
selling_price = calculate_selling_price(cost, profit_pc, overhead_pc)
print(f"\nИтоговая цена продажи мобильного телефона: ${selling_price:.2f}")