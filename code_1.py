#Name
#CIS 3301
#CODE 1 - The guessing game
import random

#Do not remove the parameter dice from the main function
def main(dice=-1):

#Use the following two lines of code for rolling the dice
    if dice == -1:
        dice = random.randint(1,6)

if __name__ == "__main__":
    main()