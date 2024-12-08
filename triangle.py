def area(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Стороны не могут образовать треугольник")
    
    # Используем формулу Герона для вычисления площади
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5
