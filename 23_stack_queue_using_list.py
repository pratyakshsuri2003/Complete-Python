
# # for Stack

# l = []
# while True:
#     user = int(input('''Enter choice: 
#                 1 - Push Element
#                 2 - Pop Element
#                 3 - Peek Elment
#                 4- Display Element
#                 5 - Exit 
#                 Type: '''))
#     if user == 1:
#         el = input("Enter the number you want to push: ")
#         l.append(el)
#         print(l)
#     if user == 2:
#         if len(l) == 0:
#             print("Empty stack!!")
#         else:    
#             l.pop()
#             print(l)
#     if user == 3:
#         if len(l) == 0:
#             print("Stack is Empty!!")
#         else:
#             print("Peeked element :"+l[-1])
#     if user == 4:
#         print(l)
#     if user == 5:
#         print("Thanks!!")
#         break

            
# for Queue

l = []
while True:
    user = int(input('''Enter choice: 
                1 - Push Element
                2 - Pop Element
                3 - front Elment
                4 - last element
                5 - Display Element
                6 - Exit 
                Type: '''))
    if user == 1:
        el = input("Enter the number you want to push: ")
        l.append(el)
        print(l)
    if user == 2:
        if len(l) == 0:
            print("Queue is Empty!!")
        else:    
            del l[0]
            print(l)
    if user == 3:
        if len(l) == 0:
            print("Queue is Empty!!")
        else:
            print("Front element :"+l[0])
    if user == 4:
        if len(l) == 0:
            print("Queue is Empty!!")
        else:
            print("Last element :"+l[-1])
    if user == 5:
        print(l)
    if user == 6:
        print("Thanks!!")
        break

