if __name__ == "__main__":
    # num1 = 12345
    # print(list(str(num1)))
    #
    # # Конструкция для разбития числа на цифры
    # digits_list = [int(d) for d in str(num1)]
    # print(digits_list)
    #
    # join_num = "".join([str(d) for d in digits_list])
    # print(int(join_num))

    a = 21345
    num_list = [int(x) for x in str(a)]
    print("1 ", num_list)
    print("2 ", sum(num_list))
    print("3 ", sum([x for x in num_list if x % 2 == 0]))
    print("4 ", len(num_list))
    print("5 ", min(num_list), max(num_list))
    print("6н ", [x for x in num_list if num_list.index(x) % 2 == 0])
    print("6ч ", [x for x in num_list if num_list.index(x) % 2 != 0])
    print("7 ", num_list[0] - num_list[-1])
    print(f"8 min: {min(num_list)} pos: {num_list.index(min(num_list)) + 1}")