if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, 3, -1, 8, 6, 9]

    # предположим, что первый элемент в нашем списке минимальный
    min_value_index = 0  # TODO чему равен индекс предполагаемого минимального элемента?
    min_value = list_[min_value_index]

    for i in range(len(list_)):  # TODO как перебрать все индексы?
        current_value = list_[i]  # TODO как получить текущий элемент по индексу?
        if current_value <= min_value:  # TODO  какое сравнение используем?
            min_value = current_value
            min_value_index = i

    print("Минимальный элемент =", min_value, "находится по индексу", min_value_index)
