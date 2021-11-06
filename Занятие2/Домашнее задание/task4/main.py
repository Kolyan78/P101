if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    max_index = 0
    max_value = list_[max_index]
    for i, current_value in enumerate(list_):
        if current_value > max_value:
            max_value = current_value
            max_index = i
    list_[0], list_[max_index] = list_[max_index], list_[0]
    print(list_)