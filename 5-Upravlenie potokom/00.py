"""
Трейдер хочет, чтобы программа проверяла, получил он прибыль или убыток по сделке
"""

price_buy = float(input("Введите цену покупки: "))
price_sell = float(input("Введите цену продажи: "))

if price_buy > price_sell:
    print(f'Трейдер в убытке на {price_sell - price_buy:.2f}$')
else:
    print(f'Трейдер в прибыли на {price_sell - price_buy:.2f}$')

