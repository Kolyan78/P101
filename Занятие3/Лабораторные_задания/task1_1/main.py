# def main():
#     a = 0
#     while True:
#         sum_ = pow(a + 1, 2) * 2
#         #print(f"Сумма квадратов {a} равна {sum_}")
#         if sum_ > 500:
#             break
#         else:
#             a += 1
#     return a

def main():
    a = 0
    list_ = []
    while True:
        if sum(list_) > 500:
            return(len(list_[:-1]))
        else:
            list_.append(a ** 2)
            print(f"Список: {list_}")
            print(f"Сумма его квадратов: {sum(list_)}")
            a += 1


if __name__ == "__main__":
    print(main())