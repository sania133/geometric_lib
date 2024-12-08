import math

# Импортируем библиотеку math

def area(r):
    """
    Вычисляет площадь круга.

    Параметры:
        r (float): Радиус круга.

    Возвращает:
        float: Площадь круга.
    """
    if r < 0:
        raise AssertionError(ValueError)
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет периметр (длину окружности) круга.

    Параметры:
        r (float): Радиус круга.

    Возвращает:
        float: Периметр круга.
    """
    if r < 0:
        raise AssertionError(ValueError)
    return 2 * math.pi * r
