def remove_whitespace(str_):
    words_list = str_.split(" ") # TODO с помощью методов строки join и split очистить строку от лишних пробелов
    words_no_empty = []
    for word in words_list:
        if len(word) !=0:
            words_no_empty.append(word)
    return " ".join(words_no_empty)


if __name__ == "__main__":
    str_with_space = "    123.    test   print test11    "  # исходная строка
    print(remove_whitespace(str_with_space))
