import circle
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
    assert fig in figs
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


