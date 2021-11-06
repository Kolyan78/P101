# def row(epsilon):
#     result = 0
#     element = 0
#     count = 1
#     while True:
#         element = 1 / (2 ** count)
#         if element > epsilon:
#             result += 1 / (2 ** count)
#             count += 1
#         else:
#             break
#     return result

def row(epsilon=0.0001):
    list_, count = [], 2
    while True:
        element = 1 / count
        if element > epsilon:
            list_.append(element)
            count *= 2
        else:
            break
    return sum(list_)

if __name__ == "__main__":
    print(row(0.0001))
