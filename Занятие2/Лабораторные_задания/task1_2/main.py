a = int(input("Введите А: "))
b = int(input("Введите B: "))
result= a % 2 != 0 and b % 2 != 0
if result:
    print("Числа A и B нечетные")
else:
    print("Одно из чисел или оба четные")