import math

def area(a, b, c):
    assert a > 0 and b > 0 and c > 0, "Стороны должны быть положительными"
    assert a + b > c and a + c > b and b + c > a, "Неверные стороны треугольника"
    
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def perimeter(a, b, c):
    assert a > 0 and b > 0 and c > 0, "Стороны должны быть положительными"
    return a + b + c

