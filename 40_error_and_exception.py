def function(a, b):
    print(a+b)


function(22,22)

# syntex error
# logical error
# ZeroDivisionError



try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("This is an divide by zero error")





