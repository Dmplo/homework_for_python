# n = 123 -> res = 6 (1 + 2 + 3)
# n = 100 -> res = 1 (1 + 0 + 0)

number = int(input())
sum = 0
while number > 0:
    digit = number%10
    sum += digit
    number = number//10

print(sum)
