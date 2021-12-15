a = int(input())
b = a //1000

b1 = b // 100
b2 = b // 10 % 10
b3 = b % 10

c = a % 1000
b4 = c // 100
b5 = c // 10% 10
b6 = c % 10

if (b1 + b2 + b3) == (b4 + b5 + b6):
    print("Счастливый")
else:
    print("Обычный")

