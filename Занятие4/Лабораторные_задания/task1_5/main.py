def ev_o_no(lst):
    even = len([x for x in lst if x % 2 == 0])
    odd = len([x for x in lst if x % 2 != 0])
    if even > odd:
        return "четных больше"
    elif even < odd:
        return "нечетных больше"
    return "равны"

if __name__ == "__main__":
    print(ev_o_no([4, -1, 10, -1, 3, -3, -6, 8, 6, 9]))

