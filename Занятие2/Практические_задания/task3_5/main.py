wind = int(input())

if 1 <= wind <= 4:
    print("Слабый")
elif 5 <= wind <= 10:
    print("Умеренный")
elif 11 <= wind <= 18:
    print("Сильный")
else:
    print("Ураганный")

