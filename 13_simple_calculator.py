
print('''**************************WELCOME TO THE PYTHON CALCULATOR*************************
        *                                                                                  *
        *                                                                                  *
        *                                                                                  *
        *********************************************************************************''')
while(True):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print('''Enter:
            '+' for Addtion
            '-' for subtraction
            '*' for multiplication
            '/' for division
            'e' for exit'''
        )
    operation = input("Enter Operation: ")
    if(operation is "+"):
        print("Addition: ",(num1+num2))
    elif(operation is "-"):
        print("Subtracion: ",(num1-num2))
    elif(operation is"*"):
        print("Multiplication: ", (num1*num2))
    elif(operation is "/"):
        print("Division: ", (num1/num2))
    elif(operation is "e"):
        print("Thanks for using this calculator")
        break
    else:
        print("please enter the mentioned operations only")               