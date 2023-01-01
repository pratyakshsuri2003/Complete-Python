class student:
    __name = "ravi" 
    def __inti__(self):
        print(self.__name)
    def printval(self, name=""):
        print("this is private"+name)

obj = student()
obj.printval()
obj.printval("Pratyaksh Suri")



class parent:
    def display(self):
        print("this is parent Class")

class child(parent):
    def display(self): # same fucntion name override the parent fucntion 
        print("This is Child Class")

obj = child()
obj.display()


class parent:
    def display(self):
        print("this is parent Class")

class child(parent):
    def display(self): # same fucntion name override the parent fucntion 
        super().display()
        print("this is child class")

obj = child()
obj.display()
