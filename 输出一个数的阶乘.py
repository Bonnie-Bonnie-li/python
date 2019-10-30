def test():
    print("请输入一个数：")
    a = int(input())
    b = 1
    if a < 0:
        print("输入的数值不能为负数")

    elif a == 0:
        print("0的阶乘为1")

    else:
        for i in range(1, a + 1):
            b = b * i
        print("{0}的阶乘为{1}".format(a, b))


if __name__ == '__main__':
    test()
