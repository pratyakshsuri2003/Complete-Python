st1 = "pratyaksh suri"
p = st1.lower()
q = st1.upper()
r = st1.title()
s = st1.capitalize()
print(p)
print(q)
print(r)
print(s)


# find() --> return index number of the substring
w = "pratyakshsuri123"
print(w.find("s"))  # returns 7 (index start from 0)

# isalpha() --> string has fully alphabetic then return true else false
print(w.isalpha())
strr = "1223"
# isdigit() --> string has fully digit then true else false
print(strr.isdigit())
# print(w.isalnum()) --> if all digits then true if all aplhabet then also true if combination of two then also true
# only give false when special character or space is used
ss = "pra@@tyaksh Su#i"
print(ss.isalnum())
print(strr.isalnum())

y = chr(65)  # --> give character according to ascii value supplied
print(y, type(y))

xx = chr(120)
print(xx, " ", type(xx))

zz = ord("x")
print(zz, type(zz))  # --> gives ascii value accori=ding to the character supplied


x = "pratyaksh"
y = "Suri"

# String Fommatting in Python

# 1. Empty placeholders
print("my first name is {} and my surname is {}.".format(x, y))
# 2. Named placeholders
print("my first name is {fname} and my surname is {lname}.".format(
    fname=x, lname=y))
