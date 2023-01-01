import re

str = "my name is Pratyaksh suri"
pattern = r"Pratyaksh"
# sub -> replace the pattern with some other(that we specify)
newStr = re.sub(pattern, "Rob", str)
print(newStr)