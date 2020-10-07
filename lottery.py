# this file will select 5 random numbers and then print them for the user
import random, os, sys

lotteryNumbers = []

def generator (lowLimit, highLimit):
    howManyNumbers = 5
    while len(lotteryNumbers) < howManyNumbers:
        x = random.randint(lowLimit, highLimit)
        if x not in lotteryNumbers:
            lotteryNumbers.append(x)
    print(sorted(lotteryNumbers))
    
generator(1, 59)       



