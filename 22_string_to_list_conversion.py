n=input('Enter the value: ')
print(n)

l = n.split() # convert the string into list 
print(l)

xx = []
for i in range(1, 6):
    take = input("Enter the value "+str(i)+" :")
    xx.append(take) # filling the elemtn in list by using append function

print(xx)    