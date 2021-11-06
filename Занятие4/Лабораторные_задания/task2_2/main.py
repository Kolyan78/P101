if __name__ == "__main__":
    a = 49
    num_list = [int(x) for x in str(a)]
    print(num_list)
    a = (4 and 8 in set(num_list) or 9 in set(num_list))
    print(a)