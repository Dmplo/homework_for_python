# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

# Пример:


# list_1 = [1, 2, 3, 4, 5]
# k = 6
# Ответ: 5

list_1 = [1, 2, 3, 4, 5, 6]
k = 6

max = list_1[0]
for i in range(1, len(list_1)):
    if max < list_1[i] and max < k:
        max = list_1[i]
print(max)