import re

pattern = r"pr.i"
# in place of . there can be any alphabet 
if re.match(pattern, "praiprsiproi"):
    print(re.findall(pattern, "praiprsiproi"))

