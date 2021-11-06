a = int(input("Введите число "))

result = a % 2 == 0 or a % 3 == 0
if result:
    print("Число кратно 2 или 3")
else:
    print("Число не кратно 2 или 3")