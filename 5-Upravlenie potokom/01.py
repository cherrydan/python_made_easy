"""
Определить, является ли введённый год високосным
"""


def is_leap_year(year):
    try:
        if year in range(1000, 2101):
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        else:
            raise ValueError
    except ValueError:
        print('Ввод завершён')
        exit(0)


if __name__ == '__main__':
    while True:
        year = int(input("Введите год(для выхода введите год меньше 1000 или больше 2100): "))
        print(is_leap_year(year))
