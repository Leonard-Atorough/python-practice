# this file will select 5 random numbers and then print them for the user
import random, os, sys

limit = 5
numbers = []


while len(numbers) < limit:
    x = random.randint(1,59)
    if x not in numbers:
        numbers.append(x)
    else:
        contine

print (sorted(numbers))
