# TODO
a = int(input("Input number A: "))
b = int(input("Input number B: "))
sk = a ** 2 + b ** 2
ks = (a + b) ** 2
if sk > ks:
    """Это усливие никогда не выполнится, так как квадрат суммы
    всегда больше чем сумма квадратов, за исключением когда оба
    или одно из чисел равны нулю, тогда они тоже будут равны"""
    print("Сумма квадратов (", sk, ") больше чем квадрат суммы (", ks, ")")
elif ks > sk:
    print("Квадрат суммы (", ks, ") больше чем сумма квадратов (", sk, ")")
else:
    print("Квадрат суммы (", ks, ") равен сумме квадратов (", sk, ")")