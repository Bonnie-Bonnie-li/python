def test():
   print("输入一个字符：")
   a=input()
   print("输入一个ascii：")
   b=int(input())
   print("{0}对应的ascii码是{1}".format(a,ord(a)))
   print("{0}对应的字符是{1}".format(b,chr(b)))


if __name__ == '__main__':
    test()