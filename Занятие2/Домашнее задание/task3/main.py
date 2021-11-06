# TODO
a = int(input())
b = int(input())
c = int(input())
result = a < 45 or b < 45 or c < 45
if result:
    print("Одно из чисел A, B или C меньше 45")
else:
    print("Все три числа больше 45")