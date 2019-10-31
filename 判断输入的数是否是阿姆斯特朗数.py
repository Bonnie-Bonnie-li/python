def test():
    print("请输入一个数：")
    a = int(input())
    n = len(str(a))
    sum = 0
    num = a
    while num > 0:
        b = num % 10
        sum = sum + b ** n
        num //= 10

    if a == sum:
        print("输入的数是阿姆斯特朗数")
    else:
        print("输入的数不是阿姆斯特朗数")


if __name__ == '__main__':
    test()
