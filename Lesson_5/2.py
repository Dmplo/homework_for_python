# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# sum(2, 2)
# # 4


a = 1
b = 999

def sum(a, b):
    if b == 1:
        return a + 1
    return 1 + sum(a, b - 1)

print(sum(a, b))


