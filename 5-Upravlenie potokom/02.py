"""

Трое сотрудников вводят с клавиатуры свой опыт работы
Вывести сотрудника с наибольшим и наименьшим опытом

"""

employees = {
    'Samir': 0,
    'Pravin': 0,
    'Mohit': 0
}

for k, v in employees.items():
    employees[k] = float(input(f'Input expirience for {k} '))



overexperienced = max(employees.values())
key = next((key for key, value in employees.items() if value == overexperienced), None)
print(f'Most experienced is {key}')

underexpierenced = min(employees.values())
key = next((key for key, value in employees.items() if value == underexpierenced), None)
print(f'Most UNexpirienced is {key}')

