from random import randint

#create a list of play options
t = ["Bear", "Ninja", "Hunter"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Bear, Ninja, or Hunter?")
    if player == computer:
        print("Tie!")
    elif player == "Bear":
        if computer == "Ninja":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Ninja":
        if computer == "Hunter":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Hunter":
        if computer == "Bear":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]