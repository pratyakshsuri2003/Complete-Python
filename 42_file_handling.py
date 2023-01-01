# writing a content to a file
f = open("write.txt", "w")
f.write("We added this line using file handling\n")
f.close()


# reading a content rfrom a file
ff = open("write.txt", "r")
content = ff.read()
print(content)
ff.close()

# appending a content to a file
f = open("write.txt", "a")
f.write("We added another this line using file handling")
f.close()

ff = open("write.txt", "r")
content = ff.read()
print(content)
ff.close()






















