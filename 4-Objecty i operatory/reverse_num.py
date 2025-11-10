def reverse_num_math(x):
    """

    Parameters
    ----------
    x - заданное число

    Returns - "перевёрнутое" число
    -------
    """
    reversed_num = 0

    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    return reversed_num


if __name__ == '__main__':
    original_number = 123456
    print(f"Заданное число {original_number} в перевёрнутом виде будет {reverse_num_math(original_number)}")
