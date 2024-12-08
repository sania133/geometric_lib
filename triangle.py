import math

def area(a, b, c):
    assert a > 0 and b > 0 and c > 0, ValueError
    assert a + b > c and a + c > b and b + c > a, ValueError
    
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def perimeter(a, b, c):
    assert a > 0 and b > 0 and c > 0, ValueError
    return a + b + c

