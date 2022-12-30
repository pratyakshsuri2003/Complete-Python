lst = []
for i in range(1, 101):
    lst.append(i) # used to add values in the empty list

print(lst)  

n = [m for m in range(1, 101) if m%2==0] # using list comprehension to add element in the em[ty list
print(n)

name = "PratyakshSuri"
s = [g for g in name]
print(s)