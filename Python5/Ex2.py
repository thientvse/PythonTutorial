class Calculator:
    a = 0
    b = 0


    def typeNumber(self):
        a = float(input("Nhap a : "))
        b = float(input("Nhap b : "))

        self.a = a
        self.b = b

    def add(self):
        print("add: "+str(self.a + self.b))

    def minus(self):
        print("minus: " + str(self.a - self.b))

    def devide(self):
        print("devide: " + str(self.a/self.b))

    def multiple(self):
        print("multiple: " + str(self.a * self.b))

    def factorial(self):
        print("multiple: " + str(self.a * self.b))

caculaltor = Calculator()
caculaltor.typeNumber()
caculaltor.add()
caculaltor.minus()
caculaltor.devide()
caculaltor.multiple()
