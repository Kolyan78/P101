def od(n):
    a = [int(x) for x in str(n)]
    return "одинаковые" if len(set(a)) == 1 else "неодинаковые"
if __name__ == "__main__":
    print(od(2222222))
