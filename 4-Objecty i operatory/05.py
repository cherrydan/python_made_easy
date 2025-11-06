def find_third_number(average_value):
    """
    Находит третье число, если среднее значение трех чисел известно,
    а первое число больше среднего настолько же, насколько второе меньше среднего.

    Аргументы:
        average_value (float/int): Среднее значение трех чисел.

    Возвращает:
        float/int: Значение третьего числа.
    """

    print(f"Дано: Среднее значение трех чисел = {average_value}")

    # Шаг 1: Найдем сумму трех чисел
    total_sum = average_value * 3
    print(f"Сумма трех чисел (A + B + C) = {average_value} * 3 = {total_sum}")

    # Шаг 2: Используем условие о первом и втором числах
    # Пусть A = average_value + X
    # Пусть B = average_value - X
    # Где X - это неизвестная разница

    # Шаг 3: Подставим выражения для A и B в уравнение суммы:
    # (average_value + X) + (average_value - X) + C = total_sum
    # average_value + X + average_value - X + C = total_sum

    # Шаг 4: Упростим уравнение (X и -X сокращаются)
    # 2 * average_value + C = total_sum
    # C = total_sum - (2 * average_value)

    third_number = total_sum - (2 * average_value)
    print(f"Из уравнения '2 * {average_value} + C = {total_sum}', получаем:")
    print(f"Третье число (C) = {total_sum} - (2 * {average_value}) = {third_number}")

    return third_number


# --- Запуск функции ---
average = 45
third_num = find_third_number(average)

print(f"\nТаким образом, третье число (C) = {third_num}")

# --- Демонстрация того, что A и B могут быть разными ---
print("\n--- Демонстрация возможных значений A и B ---")
print("Первое и второе число (A и B) не могут быть однозначно определены.")
print("Они зависят от произвольной разницы 'X'.")

test_x_values = [5, 10, 0, -8]  # Различные значения для X

for x in test_x_values:
    a_val = average + x
    b_val = average - x

    # Проверка:
    check_average = (a_val + b_val + third_num) / 3

    print(f"\nЕсли X = {x}:")
    print(f"  Первое число (A) = {average} + {x} = {a_val}")
    print(f"  Второе число (B) = {average} - {x} = {b_val}")
    print(f"  Проверка среднего: ({a_val} + {b_val} + {third_num}) / 3 = {check_average}")
    if check_average == average:
        print("  => Среднее значение совпадает с исходным. Условие выполнено.")
    else:
        print("  => Ошибка в расчетах.")