# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# Вводим длину множеств: 11 6
# Вводим превое множество: 2 4 6 8 10 12 10 8 6 4 2
# Вводим второе множество: 3 6 9 12 15 18
# Ответ: 6 12

first_size = int(input('Введите длину первого множества: '))
second_size = int(input('Введите длину второго множества: '))
first_user_list = list()
second_user_list = list()

for _ in range(first_size):
    first_user_list.append(input('Введите числа превого множества: '))

for _ in range(second_size):
    second_user_list.append(input('Введите числа второго множества: '))

first_user_set = set(first_user_list)
second_user_set = set(second_user_list)

print(first_user_set.intersection( second_user_set))