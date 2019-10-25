def number():
    try:
        a=int(input())

        if a%2==0:
           print("输入的数字是偶数")
        else:
           print("输入的数字是奇数")
    except ValueError:
        print("输入的字符类型有误")

if __name__ == '__main__':
    number()