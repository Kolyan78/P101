def is_palindrom(n):
    a = [int(x) for x in str(n)]
    if a == a[::-1]:
        return "Палиндром"
    return "Не палиндром"

if __name__ == "__main__":
    print(is_palindrom(123454321))
