try:
    a=20
    b=10
    c=1
    print(a+b/c) 
except ZeroDivisionError:
    print("This is Zero Dividion Error")
finally:
    print("This is going to execute no matter what")    