import random

target = random.randint(1,100)
while True:
    userchoice = input("guess the target or quit:")
    if(userchoice == "quit"):
        break
    userchoice = int(userchoice)
    if(userchoice == target):
        print("correct guess: successful")
        break
    elif(userchoice < target):
        print("your guess is too small guess a bigger")
    elif(userchoice > target):
        print("your guess is too big guess smaller")

print("game over")