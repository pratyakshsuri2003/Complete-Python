import datetime
x = datetime.datetime.now()
print(x)

# strftime() -> used to format string 
# %Y -> full year
# %y -> year last two digits
# %B -> full month
# %b -> month last three alphsbets
# %m -> month as a number

m = x.strftime("Year: %Y") 
print(m)