from calculator import Calculator, MoreCalculator

if __name__ == '__main__':
    a1 = Calculator(4, 0)
    b1 = MoreCalculator(4, 0)
    # c.setdata(4, 2)
    print(a1.add())
    print(a1.mul())
    print(a1.sub())
    print(a1.c)
    a1.c = 33
    print(a1.c)
    # print(a1.div())
    print(a1.a)
    print(b1.pow())
    print(b1.div())
