def test():
  for x in range(1,10):
      for y in range(1,x+1):
          b=x*y
          print('{0}*{1}={2}\t'.format(x, y, b), end='')
      print()

if __name__ == '__main__':
    test()