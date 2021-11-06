def get_new_list(lst):
    sa = sum(lst) / len(lst)
    #print(sa)
    return [round(x - sa, 2) for x in lst]
if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print(get_new_list(list_))