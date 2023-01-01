import re
# used to match strings of text such as particular characters, words, or patterns of characters
pattern = r"eggs"
# match can only search in the beggening and ending of the string 
if re.match(pattern, "hhheggshhhhhhhhhs"):
    print("Match Found !!")
else:
    print("No match Found !!")    

# search can find the matched pattern present anywhere in the string 
if re.search(pattern, "hhheggshhhhhhhhhs"):
    print("Match Found !!")
else:
    print("No match Found !!")    

print(re.findall(pattern, "hhheggshhhhhhhhhs"))



