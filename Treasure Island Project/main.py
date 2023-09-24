print("Welcome to Treasure Island. Your mission is to find the treasure?")
leftorright = input("left or right?\n")
if leftorright == "left":
    swimorwait = input("swim or wait\n ")
    if swimorwait == "swim":
        print("Attacked by trout Game Over")
    elif swimorwait == "wait":
        door = input("Which door? Red, Blue, Yello, Anything else\n").lower()
        if door == "blue":
            print("Eaten by beats/ Game Over.")
        elif door == "red":
            print("Burned by Fire. Game Over.")
        elif door == "anything else":
            print("Game Over")
        else:
            print("You Win!")
else:
    print("Fall into hole, game over!")
