def mas_de_primero(lst):
    return len([x for x in lst if x > lst[0]])
if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print(mas_de_primero(list_))