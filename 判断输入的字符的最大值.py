def test():
    try:
        a = input()
        b = input()
        c = input()
        a = float(a)
        b = float(b)
        c = float(c)
        d = [a, b, c]
        print(max(d))
    except ValueError:
        print("请输入纯数字")


if __name__ == '__main__':
    test()
