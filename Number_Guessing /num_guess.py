import random
b = random.randint(1,20)
c=0
print("GUESS GAME")
print("You have only 10 chances\n\n")
while c<10:
    a = int(input("Guess a number between 1 and 20: "))
    c=c+1
    if a==b:
        print("Yeyy! You guessed the number accurately")
        break
    else:
        if(c>=10):
            print("Your chances are over")
        else:
            print("You have",10-c," chances remaining")
