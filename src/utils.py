import random

def is_even(number):
    """
    Функция проверяет четность аргумента
    :param number: Число
    :return: True|False
    """
    return not number % 2


def get_random_number():
    return random.randint(1, 100)