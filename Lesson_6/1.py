# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


def showList(list):
    for i in list:
        print(i, end = ' ')

def calcValues(start_el, step, qty):
    list = [start_el]
    for _ in range(1,qty):
        start_el += step
        list.append(start_el)
    return list

start_el = int(input('Введите первый элемент: '))
step = int(input('Введите шаг: '))
qty = int(input('Введите количество элементов: '))
showList(calcValues(start_el, step, qty))
