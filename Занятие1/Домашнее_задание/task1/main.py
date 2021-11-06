# Напишите ваше решение
speed = int(input("Скорость, байт/сек:"))
time = int(input("Время, мин:"))
cost = int(input("Стоимость, руб/Гбайт:"))
size = (speed * time * 60) / 1024 / 1024 / 1024
print("Размер файла:", size, "Гбайт")
if size < 1:
    cost = 0
else:
    cost = (size - 1) * cost
print("Стоимость:", cost, "руб.")
