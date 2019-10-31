def test():
    print("要转化的十进制数为：")
    a = int(input())
    print("{0}的二进制数为{1}".format(a, bin(a)))
    print("{0}的八进制数为{1}".format(a, oct(a)))
    print("{0}的十六进制数为{1}".format(a, hex(a)))


if __name__ == '__main__':
    test()
