def area(a):
    """
    Вычисляет площадь квадрата.

    Параметры:
        a (float): Сторона квадрата.

    Возвращает:
        float: Площадь квадрата.
    """
    if a < 0:
        raise AssertionError(ValueError)
    return a * a


def perimeter(a):
    """
    Вычисляет периметр квадрата.

    Параметры:
        a (float): Сторона квадрата.

    Возвращает:
        float: Периметр квадрата.
    """
    if a < 0:
        raise AssertionError(ValueError)
    return 4 * a
