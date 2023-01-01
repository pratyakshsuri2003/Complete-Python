import math
# This module provides access to the mathematical functions defined by the C standard.
x = 10.2
# ceil() -> rounds of the value to one greater and always gives integer
print(math.ceil(x))

print(math.ceil(12.0))

# fabs()-> returns absolute value (always positive value returnned)
y = -123
print(math.fabs(y))

# factorial() -> gives factorial of the number
# if gives negative value to tis gives ValueError
f = 5
print(math.factorial(f))

# floor() -> rounds off value to one lesser 
xx = 9.99
print(math.floor(xx))

# fsum()-> returns sum of the list, tuple (all values must be integer)
ls = [1, 2, 3, 4,5]
print(math.fsum(ls))

# sqrt() -> Return the square root of x. 
s = 25
print(math.sqrt(s))


# pow() -> Return x**y (x to the power of y).
print(math.pow(2, 3))

# log() -> logarithmic value 
print(math.log(2))

