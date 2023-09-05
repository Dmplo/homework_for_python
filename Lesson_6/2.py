# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)

# [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

def getRangeList(start, end):
    list = []
    for i in range(start,end + 1):
        list.append(i)
    return list

def showResult(list, range_list):
    result_list = []
    for i in range(len(list)):
        if list[i] in range_list:
            result_list.append(i)
    return result_list

def showList(list):
    for i in list:
        print(i, end = ' ')

list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
range_start = int(input('Введите диапазон "от": '))
range_end = int(input('Введите диапазон "до": '))

range_list = getRangeList(range_start, range_end)
showList(showResult(list, range_list))