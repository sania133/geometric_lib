def area(side):
    if side < 0:
        raise ValueError("Сторона не может быть отрицательной")
    return side ** 2

def perimeter(side):
    if side < 0:
        raise ValueError("Сторона не может быть отрицательной")
    return 4 * side
