#from collections import Counter
def get_count_char(str_):
    # для начала переведем текст в нижний регистр
    str_ = str_.lower()  # возвращается копия
    char_dict = {}

    for char in str_:
        if char.isalpha():  # далее с помощью метода строк isalpha будем проверять, является ли символ буквой
            if char in char_dict:  # если символ уже есть среди ключей, то существующее значение увеличиваем на один
                char_dict[char] += 1
            else:  # в противном случае создаем новый элемент в словаре
                char_dict[char] = 1
    return char_dict


def frequency_chars(char_dict):
    total_count = sum(char_dict.values())

    return {char: round(value / total_count, 3) for char, value in char_dict.items()}

def asd(str_):
    str_ = str_.lower()
    for char in str_:
        if char.isalpha():
            print(char)

if __name__ == "__main__":
    main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """
    #asd(main_str)
    print(get_count_char(main_str))
    #print(frequency_chars(get_count_char(main_str)))
