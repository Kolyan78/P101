if __name__ == "__main__":
    rus_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    #help(enumerate)
    for index, value in enumerate(rus_alphabet, start=1):  # TODO как за один раз получать пару индекс-значение?
        print(index, value)  # TODO как тогда должен выглядеть индекс?
