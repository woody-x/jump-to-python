class Calculator:
    a = 1
    b = 1
    c = 1
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def setdata(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def sub(self):
        return self.a - self.b

    def div(self):
        return self.a / self.b

class MoreCalculator(Calculator):
    def pow(self):
        return self.a**self.b
    def div(self):
        if self.b == 0:
            return 0
        else:
            return self.a/self.b

