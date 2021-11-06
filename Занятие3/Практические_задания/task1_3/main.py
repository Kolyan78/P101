def incorrect_func(name_arg=[]):
    # name_arg является локальной переменной
    print("Аргумент до изменения", name_arg)
    name_arg.append(1)
    print("Аргумент после изменения", name_arg)


def incorrect_main():
    # вызовем два раза одну и ту же функцию
    incorrect_func()
    print('-----')
    incorrect_func()


# установим аргумент name_arg пустым а внутри функции будем проверять его
def correct_func(name_arg=None):
    if name_arg is None:
        name_arg = []
    print("Аргумент до изменения", name_arg)
    name_arg.append(1)
    print("Аргумент после изменения", name_arg)


def correct_main():
    # вызовем два раза одну и ту же функцию
    correct_func()
    print('-----')
    correct_func()
    print('-----')
    correct_func([123])
    print('-----')
    correct_func(name_arg=[123])


if __name__ == "__main__":
    incorrect_main()
    correct_main()
