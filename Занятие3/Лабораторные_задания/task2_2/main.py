def is_palindrom(str_):
    str1_ = ""
    for i in range(len(str_)):
        if str_[i] != " ":
            str1_ += str_[i]
    str1_ = str1_.lower()
    str2_ = str1_[-1:-len(str1_) - 1:-1]
    if str1_ == str2_:
        return "Палиндром"
    else:
        return "Не палиндром"

if __name__ == "__main__":
    print(is_palindrom("А  роза упала на   лапу Азора"))
