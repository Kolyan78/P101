def get_kol(list_):
    return len([x for x in list_ if x % 2 == 0])
if __name__ == "__main__":
    print(get_kol([2, 4, 7, 1, 4, 9, 1, 8]))
