list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3]

count_even = 0  # количество четных чисел
count_odd = 0  # количество нечетных чисел
for i in list(range(len(list_))):
    if list_[i] % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
# TODO посчитать количество четных и нечетных значений в списке

if count_even > count_odd:
    print('Четных чисел больше')
else:
    print('Нечетных чисел больше')
