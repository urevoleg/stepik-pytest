import typing as t

def add(a: t.Any, b: t.Any) -> t.Any:
    """
    :param a: [int|float|decimal]
    :param b: [int|float|decimal]
    :return: sum of two numbers
    """
    return a + b


def divide(a, b):
    """
    Эта функция делит a на b.
    Вызывает ValueError при делении на ноль.
    """
    if b == 0:
        raise ValueError("Нельзя делить на ноль")
    return a / b