def func(str1):
    str1 = str1.split(" ")
    #str2 = []
    for word in str1:
        if len(word) != 0:
            print(word)
            #str2.append(word)


if __name__ == "__main__":
    func("Художника   обидеть            может каждый")
