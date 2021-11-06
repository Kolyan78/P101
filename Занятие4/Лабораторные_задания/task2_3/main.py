def num2(n):
    a = [int(x) for x in str(n)]
    if 9 < sum(a) < 100:
        return "Двузначное"
    return "Однозначное"
if __name__ == "__main__":
    print(num2(999))
