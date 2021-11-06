def get_sqrt(n, m):
    return [x ** 2 for x in range(n, m+1) if x % 2 == 1]
if __name__ == "__main__":
    print(get_sqrt(5, 13))
