def pow_func(base, pow_=2):
    # base ** pow_ -> реализовать через цикл while
    result = 1
    while pow_ > 0:
        result *= base
        pow_ -= 1
    return result


if __name__ == "__main__":
    a = 5
    n = 3

    print(pow_func(a, n))
