import pickle
ls = [1, 2, 3, 4, 5]
file = open("write.txt", "wb")
pickle.dump(ls, file)
file.close()

file = open("write.txt", "rb")
l = pickle.load(file)
print(l)