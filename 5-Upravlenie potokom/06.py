"""
Напишите программу, для вывода таблицы умножения любого заданного числа
"""
try:
    i = int(input('Введите число '))
    for k in range(1, 11):
        print(f'{i} * {k} = {i * k}', end=' | ')
except ValueError:
    print("Ошибка ввода")
    exit(-1)

finally:
    print('\nПрограмма завершена')
