number = 123

d_1 = number // 100 # TODO найти число сотен
d_2 = number % 100 // 10 # TODO найти число десятков
d_3 = number % 10 # TODO найти число единиц

list_digit = [d_1, d_2, d_3]  # TODO сформировать список чисел
print(list_digit)

print("Сумма цифр", sum(list_digit))  # TODO сумма цифр
print("Количество цифр", len(list_digit))  # TODO количество цифр
print("Минимальная цифра", min(list_digit))  # TODO минимальная цифра
print("Максимальная цифра", max(list_digit))  # TODO максимальная цифра
