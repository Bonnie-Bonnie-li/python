def test():
    print("请输入第一个数字:")
    a = int(input())
    print("请输入第二个数字:")
    b = int(input())
    if a > b:
        print("未按照由小到大的顺序输入数字")
        return
    for i in range(a, b):
        for n in range(2, i):
            if i % n == 0:
                break
        else:
            print(i)
if __name__ == '__main__':
    test()
