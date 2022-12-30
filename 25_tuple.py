# ordered datatype 
# immutable


t = (1, 2, 3, 4,4, 4,4,4, 5, 6, 7, 8, 9)
print(t[2]) # returns value from the given index
print(t.index(3)) # returns index of the given value
print(t.count(4)) # count the ocuurences of an element
print(type(t))
# tuple must have more than one element inside it otherwise it will not be called tuple.
# for tuple atleast two elements must be their inside it
t1 = (1)
print(type(t1))
t2 = ("Pratyaksh")
print(type(t2))