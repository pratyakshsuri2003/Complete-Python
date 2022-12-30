# unordered datatype 
# un indexed
# can only store unique elements
s = {1, 2, 3, 4, 5}
print(type(s))

# set() -> can convert list to set 

l = [1, 2, 3, 4, 5]
print(l)
st = set(l)
print(st)
# add() --> adds data

st.add(6)
st.add(7)
print(st)
# pop() --> removes data
# (fifo)
st.pop()
print(st)

# remove() --> remove specific data
st.remove(5)
print(st)

# discard() -> removes specific data
st.discard(6)
print(st)
# update() -> update set by adding new unique values at the end
lll = [10, 20 ]
st.update(lll)
print(st)
# clear() -> clear the whole set

st.clear()
print(st)