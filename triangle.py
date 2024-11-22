import math
def area(a, b, c):
    """Вычисляет площадь треугольника по формуле Герона."""
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
def perimeter(a, b, c):
    """Вычисляет периметр треугольника."""
    return a + b + c


