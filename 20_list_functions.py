# function to delete element from the list

lt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lt)
del lt[4]  # delete 5 (4th index element) from the list
print(lt)

# pop() --> delete the element from the list and also return the deleted value
lt.pop(2)  # delete 3 from the list (3rd indexed element)
print(lt)

# lt.remove() --> used to delete perticular value

ls = [11, 22, 56, 23, 78, 90]
ls.remove(56)
print(ls)

ll = [1, 2, 3]
# clear() --> it delete all the content and return the empty list
ll.clear()
print(ll)

# functions for update element from the list
# insert() --> used to insert
lf = [1, 2, 3]
lf.insert(11, 2)
print(lf)
lf.append(110)
print(lf)
# extend() --> extend works on the values inside the list
lll = [11, 22, 33]
fff = [66, 77]
print("Appending...")
lll.append(fff)
print(lll)
lll = [11, 22, 33]
fff = [66, 77]
print("Extending...")
lll.extend(fff)
print(lll)

# count() --> counts how many times an element present in the list.
x = [10, 20, 30, 40, 10]
print(x.count(10))

# max() -> gives maximum Value from the list
# min() -> gives minimum value from the list 
# sort() -> used to sort the list
x.sort()
print(x)
# reverse() -> reverse the element of the list
x.reverse()
print(x)

# index() -> gives the index no the elemnt 
print(x.index(30))