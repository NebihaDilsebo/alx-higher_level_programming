#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if last digit of a number > 5:
    print(f"Last digit of {number} is [:4] and is greater than 5")
elif last digit of number == 0:
    print(f"Last digit of {number} is [:4] and is 0")
else:
    print(f"Last digit of {number} is [:4] and is less than 6 and not 0")
