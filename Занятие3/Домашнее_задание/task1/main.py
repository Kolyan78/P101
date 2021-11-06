if __name__ == "__main__":
    list_ = []
    while True:
        a = int(input("Введите число:"))
        if a < 0:
            break
        elif 3 <= a <= 13:
            list_.append(a)
    print(list_)