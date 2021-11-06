if __name__ == "__main__":
    cart = {
        "apple": 80,
        "orange": 65,
        "banana": 40
    }
    # sum_ = 0
    # # TODO посчитать через ключи
    # for fruit in cart.values():
    #     print(fruit)  # получаем значение по ключу
    #     sum_ += fruit
    # print(sum_)

    print(sum(cart.values()))
    # TODO посчитать через метод values
