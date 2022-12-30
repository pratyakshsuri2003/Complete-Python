def printthename():
    print("Pratyaksh")

def greet(name, id):
    print("Hello {} how are you? your college id is {} ...".format(name, id))
# using placeholders in print statemnet is a good habit:)
# printthename()
# n = input("Enter your name: ")
# i = input("Enter your id: ")
# greet(n, i)


def sum(a,b):
    return a+b


def fact(n):
    if n<0:
        return "Factorial not exist"
    elif n==0:
        return 1
    else:
        return n*fact(n-1)
a = 10
b = 20
print(fact(2))
# print(sum(a,b)) 







