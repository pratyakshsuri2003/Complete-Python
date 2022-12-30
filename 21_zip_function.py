l = [10, 20, 30 ,40]
l2 = [3, 4, 77, 12, 19, 13]
for a,b in zip(l, l2):
    print(a, b)

''' zip() -> used to itrate two or more list or tuples
but there must be same number of element present in the lists 
otherwise the common will be print and rest will be ignored '''

length = len(l)
for i in range(length):
    print(l[i], l2[i])

    # same work can be done by using other methods as well... 