# str_ = "car"
# width = 6
# #print(str_.rjust(width, "-"))
def print_matrix(a, b):
    matrix = [list(range(1, a + 2))] * (b + 1)
    p = len(str(a * b))
    for i in range(1, len(matrix)):
        if i == 2:
            print("-" * ((a * (p + 1)) + 2))
        for j in range(1, len(matrix[0])):
            matrix[i][j] = i * j
            print(str(matrix[i][j]).rjust(p, " "), end=" ")
            if j == 1:
                print(":", end=" ")
        print()
print_matrix(9, 9)
