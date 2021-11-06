def func(a, b):
    result = b
    #print(f"1 месяц: расходы - {b}, итого - {result}")
    for i in list(range(2, 11)):
        b *= 1.03
        result += b
        #print(f"{i} месяц: расходы - {round(b, 2)}, итого - {round(result, 2)}")
    return round(result, 2)

def func2(a, b):
    result, mes = b, 1
    while True:
        if 10 >= mes > 1:
            b *= 1.03
            result += b
        #print(f"{mes} месяц: расходы - {round(b, 2)}, итого - {round(result, 2)}")
        mes += 1
        if mes > 10:
            break
    return round(result, 2)

if __name__ == "__main__":
    print(func(1000, 2000))
    print(func2(1000, 2000))
