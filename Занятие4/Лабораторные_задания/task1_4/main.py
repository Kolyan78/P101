def get_new_list(lst):
    sr = sum(lst) / len(lst)
    return [x for x in lst if x > sr]

if __name__ == "__main__":
    print(get_new_list([2, 6, 9, 1, 3, 4, 125]))
