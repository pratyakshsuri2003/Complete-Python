
def enev_numbers(x):
    for i in range(x):
        if i%2==0:
            yield i

print(list(enev_numbers(31)))