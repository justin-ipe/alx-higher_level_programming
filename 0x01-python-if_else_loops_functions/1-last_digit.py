#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_d = number % -10
else:
    last_d = number % 10
str = f"Last digit of {number} is {last_d}"

if number >= 0:
    if last_d > 5:
        print(f"{str} and is greater than 5")
    elif last_d == 0:
        print(f"{str} and is 0")
    elif last_d < 6 and last_d != 0:
        print(f"{str} and is less than 6 and not 0")
else:
    last_d = number % -10
    str = f"Last digit of {number} is {last_d}"
    print(f"{str} and is less than 6 and not 0")
