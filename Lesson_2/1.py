# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# 5 -> 1 0 1 1 0
# 2

n = int(input("Enter the number of coins: "))
headsCount = 0
tailsCount = 0

for _ in range(n):
    side = int(input('side: '))
    if side == 0:
        headsCount += 1
    elif side == 1:
        tailsCount += 1

print(f"Solution: {tailsCount if headsCount > tailsCount else headsCount}")