class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print("First Name: {} | Last Name: {}.".format(self.firstname, self.lastname))


class child(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
        print("graduatio Year: ", self.graduationyear)

x = Person("Pratyaksh", "Suri")
x.printname()

y = child("Hello", "Hi", 2023)
print(y.graduationyear)

# here child is the child class of Person class 