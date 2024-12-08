import math


def area(radius):
    if radius < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * (radius ** 2)

def perimeter(radius):
    if radius < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 2 * math.pi * radius
