def test():
    try:
        a = int(input())
        if a < 1:
            print("{0}不是质数".format(a))
        else:
            for i in range(2, a):
                if a % i == 0:
                    print("{0}不是质数".format(a))

                    return
                else:
                    print("{0}是质数".format(a))
                    break


    except:
        print("请输入数字")


if __name__ == '__main__':
    test()
