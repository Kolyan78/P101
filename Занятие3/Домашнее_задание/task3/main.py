def func(str1):
    str1 = str1.split(" ")
    str3 = [] #здесь будет список самых длинных слов
    max_len = 1 #максимальная длина слова
    for word in str1:
        lword = len(word) #длина слова
        if lword != 0:
            if lword > max_len: #проверим длину слова, не превышает ли его длина максимальную
                max_len = lword #если превышает, то список самых длинных слов обнулить и к нему прибавить новое длинное слова
                str3 = []
                str3.append(word)
            elif lword == max_len: #если длина не превышает, до пополнить список самых длинных слов
                str3.append(word)
    if len(str3) == 1:
        return str3[0]
    else:
        return str3

if __name__ == "__main__":
    print(func("Слово  функция строка список цикл переменная константа оператор кортеж постоянная"))

