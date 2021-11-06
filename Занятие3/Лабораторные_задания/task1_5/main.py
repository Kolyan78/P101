def looking_for_the_sum():
    list_ = []
#    a = None
    while True:
        a = int(input("Введите любое число (0 - для прекращеня ввода): "))
        if a == 0:
            break
        elif a < 0:
            continue
        else:
            list_.append(a)
    return sum(list_)

if __name__ == "__main__":
    print(looking_for_the_sum())
