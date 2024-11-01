# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## File circle.py
```import math
'''импортирует библиотеку math'''
def area(r):
'''Принимает аргумент r - радиус круга и возвращает площадь круга'''
    return math.pi * r * r
def perimeter(r):
'''Принимает аргумент r - радиус круга и возвращает периметр круга'''
    return 2 * math.pi * r
```
## File square.py
```def area(a):
'''Принимает переменную а - сторону квадрата, возвращает площадь квадрата'''
    return a * a

def perimeter(a):
'''Принимает переменную а - сторну квадрата, возвращает площадь квадрата'''
    return 4 * a
```
## File triangle.py
```def area(a, b, c):
'''Функция area принимает три переменные - a,b,c, и возвращает полусумму чисел a,b,c'''
    return (a + b + c) / 2

def perimeter(a, b, c):
'''Функция perimetr примимает три переменные - a,b,c - стороны треугольника, и возвращает перимент этого треугольника'''
    return a + b + c
```
## File calculate.py
```import circle
import square
'''Импортируем модули circle и square, которые содержат функции для вычисления площади и периметра соответствующих фигур'''
figs = ['circle', 'square']
'''Создает список доступных фигур'''
funcs = ['perimeter', 'area']
'''Создает список доступных функций'''
sizes = {}
'''Создает словарь sizes, который будет использоваться для хранения информации о размерах фигур'''
def calc(fig, func, size):
'''Задаем функцию calc, которая принимает параметры fig - название фигуры, func - название функции, size - список значений, необходимых для вычислений, и печатает результат выполнения функции func из модуля fig'''
    assert fig in figsgit 
    assert func in funcs
    result = eval(f'{fig}.{func}(*{size})')
    print(f'{func} of {fig} is {result}')
if __name__ == "__main__":
'''Этот блок кода выполняется только тогда, когда файл запущен как основная программа'''
    func = ''
    fig = ''
    size = list()
    while fig not in figs:
       fig = input(f"Enter figure name, avaliable are {figs}:\n")
    while func not in funcs:
       func = input(f"Enter function name, avaliable are {funcs}:\n")
    while len(size) != sizes.get(f"{func}-{fig}", 1):
       size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
'''Циклы работают, если пользователь ввел некорректное название функции или фигуры или недостаточное количество аргументов'''
    calc(fig, func, size)
```
# Area
## Описание
Функция вычисляет площадь круга
## Параметры
* r - радиус круга
## Возвращает значение 
*  Площадь круга
## Примеры
* >area(5)
  > >78.53981633974483
# perimeter
## Описание
Функция вычисляет периметр круга
## Параметры
* r - радиус круга
## Возвращает значение 
*  Периметр круга
## Примеры
* >perimeter(5)
  > >31.415955359
# Area
## Описание
Функция вычисляет площадь квадрата
## Параметры
* a - сторона квадрата
## Возвращает значение 
*  Площадь квадрата
## Примеры
* >area(2)
  > >4
# perimeter
## Описание
Функция вычисляет периметр квадрата
## Параметры
* a - сторона квадрата
## Возвращает значение 
* Периметр квадрата
## Примеры
* >perimeter(2)
  > >8

#History
Mon Oct 21 00:09:02 2024 +0300|883cbfd|Alexandra Smirnova <smirnovaad13@gmail.com>|Documentation to calculate.py added
Sun Oct 20 23:43:53 2024 +0300|08aa62e|Alexandra Smirnova <smirnovaad13@gmail.com>|Documentation to triangle.py added
Sat Oct 19 21:10:02 2024 +0300|2c07fa|Alexandra Smirnova <smirnovaad13@gmail.com>|Documentation to square.py added
Sat Oct 19 21:05:12 2024 +0300|d2723e|Alexandra Smirnova <smirnovaad13@gmail.com>|Documentation to circle.py added
Tue Mar 30 18:02:23 2021 +0300| b5b0fae|Daniil.K <dlkay@yandex.ru>|Update docs for calculate.py
Tue Mar 30 17:57:42 2021 +0300| d76db2a|Daniil.K <dlkay@yandex.ru> |Add calculate.py
Fri Mar 26 14:52:26 2021 +0300| 51c40eb|smartiqa <info@smartiqa.ru>|Doc updated for triangle
Fri Mar 26 14:48:39 2021 +0300|d080c78|smartiqa <info@smartiqa.ru>|Triangle added
Thu Mar 4 14:55:29 2021 +0300|d078c8d|smartiqa <info@smartiqa.ru>|Docs added
Thu Mar 4 14:54:08 2021 +0300|8ba9aeb|smartiqa <info@smartiqa.ru>|Circle and square added