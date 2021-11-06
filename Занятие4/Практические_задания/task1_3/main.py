def func(lst):
    return [x ** 2 if x % 2 ==0 else -x for x in lst]

if __name__ == "__main__":
    list_ = [i for i in range(10)]  # TODO
    print(func(list_))


