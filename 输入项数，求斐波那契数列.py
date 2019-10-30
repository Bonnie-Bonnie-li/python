def test():
    print("需要的项数：")
    a = int(input())
    x = 0
    y = 1
    for i in range(1, a + 1):
        print(x, end=",")
        x = x + y
        y = x - y
if __name__ == '__main__':
    test()
