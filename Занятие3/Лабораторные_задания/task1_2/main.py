# def factorial(n):
#     fact = 1
#     for i in list(range(n)):
#         fact *= (i + 1)
#     return fact

def factorial(n):
    fact = 1
    count = 2
    while count <= n:
        fact *= count
        count += 1
    return fact

if __name__ == "__main__":
    print(factorial(5))
