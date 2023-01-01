def add(x):
    return x+2

newlist = [10, 20, 30, 40, 50]
res = list(map(add, newlist))
print(res)