# mutable datatypes:
                    # list
                    # Dictionary
                    # byte array
# immutable datatypes:
                    # int
                    # float
                    # complex
                    # string
                    # tuple
                    # set
a = 5
print(type(a))
b = 34.56
print(type(b))
lt = [1, 2, 3]
print(type(lt))
dict = {"name": "Pratyaksh Suri",  # key value pairs # unordered
        "rollno": 2002276,
        "Branch": "Mechanical(Computer Science)"}
print(type(dict))
singleline_string = "Somthing" 
print(type(singleline_string))
multiline_string = '''heee jjjeelkdcxll
                      cdkmxmcn
                      ckn,kmcxnv,mvn'''
print(type(multiline_string))
tup = (1, 2, 3, 7, 4)
print(type(tup))
dict["rollno"] = 23
print(dict["rollno"])
st = "thisisstring"
# st[1] = 'p' # generates an error as strings are immutable datatype
# print(st)
s1 = {11, 11, 3, 4, 5} # unordered and # unique value only (if duplicate values are there than it automatically removes it)
print(s1)
print(type(s1)) 
# s1[2] = 12 # # generates an error as set are immutable datatype
# print(s1)
