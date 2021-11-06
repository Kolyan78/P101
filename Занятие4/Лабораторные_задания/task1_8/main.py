def get_new_list(lst):
    return[x ** 3 if x >= 0 else 0 for x in lst]

if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print(get_new_list(list_))