import random

# randint() -> takes two arguement and returns a number between them randommly
print(random.randint(2, 9))

# choice() -> Choose a random element from a non-empty sequence.
l = list('Pratyaksh Suri')
print(l)
print(random.choice(l))

# random() -> return x in the interval [0, 1).
print(random.random())

# shuffle()->Shuffle list x 
lstt = [12, 11, 15, 14, 18]
print(lstt)
random.shuffle(lstt)
print(lstt)

# uniform() -> retuns random float betwen two given parameters
print(random.uniform(1, 2))