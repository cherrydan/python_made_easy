"""
сенерируйте все трезначные цифры, разряды которых состоят из 1..3
"""
counter = 0

for i in range(1, 4):
    for k in range(1, 4):
        for l in range(1,4):
            print(i, k, l, sep='', end=' ')
            counter += 1

print()
print(f'Всего получилось {counter} таких чисел')
