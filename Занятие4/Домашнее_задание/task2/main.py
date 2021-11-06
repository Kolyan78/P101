def od2(n):
    a = [int(x) for x in str(n)]
    return "Есть одинаковые" if len(set(a)) != len(a) else "Все разные"

if __name__ == "__main__":
    print(od2(123451))
