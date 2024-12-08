import math

def calc(shape, operation, dimensions):
    # Проверка на количество параметров для каждой фигуры
    if shape == 'circle':
        assert len(dimensions) == 1, "Circle requires 1 parameter (radius)"
        radius = dimensions[0]
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        if operation == 'area':
            return math.pi * (radius ** 2)
        elif operation == 'perimeter':
            return 2 * math.pi * radius
        else:
            raise ValueError("Invalid operation for circle")

    elif shape == 'square':
        assert len(dimensions) == 1, "Square requires 1 parameter (side length)"
        side = dimensions[0]
        if side < 0:
            raise ValueError("Side length cannot be negative")
        if operation == 'area':
            return side ** 2
        elif operation == 'perimeter':
            return 4 * side
        else:
            raise ValueError("Invalid operation for square")

    elif shape == 'triangle':
        assert len(dimensions) == 3, "Triangle requires 3 parameters (side lengths)"
        a, b, c = dimensions
        if a < 0 or b < 0 or c < 0:
            raise ValueError("Side lengths cannot be negative")
        # Проверка на существование треугольника
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides")
        # Площадь по формуле Герона
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        if operation == 'area':
            return area
        elif operation == 'perimeter':
            return a + b + c
        else:
            raise ValueError("Invalid operation for triangle")

    else:
        raise AssertionError("Invalid shape")

