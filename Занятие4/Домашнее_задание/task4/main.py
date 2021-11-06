def happy(n):
    a = [int(x) for x in str(n)]
    return "Счастливый" if sum(a[0:3]) == sum(a[3:]) else "Несчастливый"

if __name__ == "__main__":
    print(happy(123231))
