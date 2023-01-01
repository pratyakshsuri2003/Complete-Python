# class student:
#     def __init__(self):
#         self._name = ""
#     def getname(self): # used to get the name
#         return self._name
#     def setname(self, name): # used to set the name
#         self._name = name



# oj = student()
# oj.setname("Pratyaksh")
# print(oj.getname())


class student:
    __name = "ravi" # two underscore used to make private variable
    def __inti__(self):
        print(self.__name)
    def __printval(self):
        print("this is private")


obj = student()
# print(obj.__name)
obj.__printval()
# print(dir)


