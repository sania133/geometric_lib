# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

## File circle.py
- import math - Эта строка импортирует библиотеку math.pi. Библиотека math.pi предоставляет доступ к математическим константам и функциям, в нашем случае требуется число Пи.
- def area(r): - Создает функцию под названием area, которая принимает аргумент r(радиус круга).
- return math.pi * r * r - Эта строка вычисляет площадь круга. math.pi - это константа, число Пи. return возвращает результат вычисления из функции area.
- def perimeter(r): - Создает функцию под названием perimeter, которая принимает аргумент r (радиус круга).

- return 2 * math.pi * r - Эта строка выполняет вычисление периметра круга. 2 * math.pi * r -  вычисляет длину окружности. return возвращает результат вычисления  из функции perimeter.

## File square.py
- def area(a): - Создает функцию под названием area, которая принимает аргумент a(сторона квадрата).
- return a * a -  Вычисляет квадрат числа a. return возвращает результат вычисления из функции area.
- def perimeter(a): -  Определяет функцию с именем perimeter, которая принимает аргумент a(сторона квадрата).
- return 4 * a - Вычисляет периметр квадрата. return возвращает результат вычисления из функции perimeter.

## File triangle.py
- def area(a, b, c): - Определяет функцию с именем area, которая принимает три аргумента: a, b и c.
- return (a + b + c) / 2 - Вычисляет сумму трех чисел a, b и c (a + b + c), а затем делит результат на 2. return возвращает результат вычисления из функции area.
- def perimeter(a, b, c): - Определяет функцию с именем perimeter, которая также принимает три аргумента: a, b и c.
-  return a + b + c - Вычисляет сумму трех чисел a, b и c (a + b + c). return возвращает результат вычисления из функции perimeter.

## File calculate.py
- import circle, import square - Эти строки импортируют модули circle и square, которые, предположительно, содержат функции для вычисления периметра и площади соответствующих фигур.
- figs = ['circle', 'square'] - Создает список доступных фигур (circle и square).
- funcs = ['perimeter', 'area'] -  Создает список доступных функций (perimeter и area).
- sizes = {} - Создает пустой словарь sizes, который в будущем, возможно, будет использоваться для хранения информации о размерах фигур.
-  Определяет функцию calc, которая принимает три аргумента:
- fig -  Название фигуры (например, circle).
- func -  Название функции (например, perimeter).
- size - Список значений, необходимых для вычисления (например, радиус круга или сторона квадрата).
- assert fig in figs -  Проверяет, существует ли фигура fig в списке figs. Если нет, то программа завершится с ошибкой.
- assert func in funcs -  Проверяет, существует ли функция func в списке funcs. Если нет, то программа завершится с ошибкой.
- result = eval(f'{fig}.{func}(*{size})') - Вычисляет результат функции func из модуля fig. 
- f'{fig}.{func}(*{size})'  - это строка, которая формируется в зависимости от значений fig, func и size.
- eval() -  выполняет строку как Python-код,  в результате чего вызывается функция func из модуля fig с передачей значений size.
- print(f'{func} of {fig} is {result}') - Выводит на экран результат вычислений.
- if __name__ == "__main__": - Этот блок кода выполняется только тогда, когда файл запущен как основная программа. 
- func = '' -  Инициализирует переменную func пустой строкой.
- fig = '' -  Инициализирует переменную fig пустой строкой.
- size = list() -  Создает пустой список size.
- while fig not in figs: -  Цикл повторяется, пока пользователь не введет корректное название фигуры.
- fig = input(f"Enter figure name, avaliable are {figs}:\n") - Запрашивает у пользователя название фигуры и сохраняет его в переменную fig.
- while func not in funcs: - Цикл повторяется, пока пользователь не введет корректное название функции.
- func = input(f"Enter function name, avaliable are {funcs}:\n"): Запрашивает у пользователя название функции и сохраняет его в переменную func.
- while len(size) != sizes.get(f"{func}-{fig}", 1) - Цикл повторяется, пока пользователь не введет корректное количество размеров для выбранной фигуры и функции. 
- sizes.get(f"{func}-{fig}", 1)  -  пытается получить значение из словаря sizes по ключу  f"{func}-{fig}".
- size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' '))) - Запрашивает у пользователя размеры фигуры, разделенные пробелами, и преобразует их в целые числа.
- calc(fig, func, size) -  Вызывает функцию calc с полученными от пользователя данными.

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
Mon Oct 21 03:25:52 2024 +0300|91bf5a4|Alexandra Smirnova <smirnovaad13@gmail.com>|Documentation to calculate.py added
Sun Oct 20 23:43:53 2024 +0300|7672585|Alexandra Smirnova <smirnovaad13@gmail.com>|Documentation to triangle.py added
Sat Oct 19 21:10:02 2024 +0300|c68e4d8|Alexandra Smirnova <smirnovaad13@gmail.com>|Documentation to square.py added
Sat Oct 19 21:05:12 2024 +0300|7e78ccf|Alexandra Smirnova <smirnovaad13@gmail.com>|Documentation to circle.py added
Tue Mar 30 18:02:23 2021 +0300|b5b0fae|Daniil.K <dlkay@yandex.ru>|Update docs for calculate.py
Tue Mar 30 17:57:42 2021 +0300|d76db2a|Daniil.K <dlkay@yandex.ru> |Add calculate.py
Fri Mar 26 14:52:26 2021 +0300|51c40eb|smartiqa <info@smartiqa.ru>|Doc updated for triangle
Fri Mar 26 14:48:39 2021 +0300|d080c78|smartiqa <info@smartiqa.ru>|Triangle added
Thu Mar 4 14:55:29 2021 +0300|d078c8d|smartiqa <info@smartiqa.ru>|Docs added
Thu Mar 4 14:54:08 2021 +0300|8ba9aeb|smartiqa <info@smartiqa.ru>|Circle and square added