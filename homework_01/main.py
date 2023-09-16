"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args: int):
    """
    Функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    [1, 4, 25, 49]
    """
    return [num ** 2 for num in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num: int):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def filter_numbers(numbers: list, filter_string: str):
    """
    Функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    [2, 4]
    """
    match filter_string:
        case "prime":
            return list(filter(is_prime, numbers))
        case "even":
            return list(filter(lambda num: num % 2 == 0, numbers))
        case "odd":
            return list(filter(lambda num: num % 2 != 0, numbers))
