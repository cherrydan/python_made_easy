"""

вывести все простые числа от 1 до 50

"""
import math
import pprint


def find_primes_up_to_n(n):
    """

    Parameters
    ----------
    n - ограничитель нашего поиска простых чисел

    Returns = list of primes numbers
    -------

    """

    prime_numbers = []  # список для хранения найденных простых чисел
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers


if __name__ == '__main__':
    limit = 50
    primes_found = find_primes_up_to_n(limit)
    print(primes_found)