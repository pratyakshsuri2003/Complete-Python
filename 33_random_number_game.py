import random


# random number game
while(True):
    print("Welcome to Number Guessing Game ...")
    wannaplay = int(input('''Choose one: 
            1 - Play
            2 - Exit
            : '''))      
    if(wannaplay == 1):
        r = random.randint(1, 100)
        count = 0
        while(True):
            u = int(input("Enter your guess: "))
            if(u<r):
                print("Guess Higher !!")
                count = count+1
            elif(u>r):
                print("Guess Lower !!")
                count = count+1
            elif(u==r):
                print("You guessed it right !!")
                count = count+1
                break
        print("Number of Guess Used: ", count)
    if(wannaplay == 2):
        print("Thanks for Playing this Game !!") 
        break   