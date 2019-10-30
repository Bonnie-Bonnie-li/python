def test():
    a=0
    b=1
    while b < 50:
        print(b,end=",")
        b=a+b
        a=b-a
if __name__ == '__main__':
    test()