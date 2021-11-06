def pm(n):
    list_ = []
    mn = 2
    while n != mn:
        if n % mn == 0:
            n = n / mn
            list_.append(mn)
        else:
            mn += 1
    list_.append(mn)
    return list_

if __name__ == "__main__":
    print(pm(87))
