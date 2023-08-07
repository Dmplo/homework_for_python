# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

number = int(input())

i = 0
result = 0
while True:
    result = 2**i
    if result > number:
        break
    print(result) 
    i += 1