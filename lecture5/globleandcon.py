#This program simulastes 10 tosses of a coin.
import random

#constants
HEADS = 1
TAILS = 2
TOSSES = 10
def tosses_coin():
    for toss in range(TOSSES):
        #simulate the coin toss.
        if random.randint(HEADS, TAILS) == HEADS:
            print("Heads")
        else:
            print("Tails")
#call the main function
tosses_coin()