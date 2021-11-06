def task(str1, str2, k):
    if str1[:k] == str2[:k]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    task("Hello, world!!!", "Hello world!!!", 5)
