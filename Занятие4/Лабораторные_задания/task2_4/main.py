def x7(n):
    a = [int(x) for x in str(n)]
    if sum(a) % 7 == 0:
        return "Кратно"
    return "Некратно"

if __name__ == "__main__":
    print(x7(1992))
