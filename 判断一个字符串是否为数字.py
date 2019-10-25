def is_number():
    a=input()
    try:
        float(a)
        print(True)
    except ValueError:
        print(False)

if __name__ == '__main__':
    is_number()