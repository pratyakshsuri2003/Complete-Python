class DemoClass: # camel-case
    a=10
    def showvalue(self):
        c = self.a*self.a*self.a
        print(c)
    def greet(self, name):
        print("Hello {}. How are your ? ".format(name))

    def sumAndmul(self, a, b):
        print("Sum: ", a+b, " Mul: ", a*b)


od = DemoClass()
od.showvalue()
od.greet("Pratyaksh")
od.sumAndmul(5, 4)
# ob = DemoClass()
# print(ob.a) # to print a from a DemoClass
