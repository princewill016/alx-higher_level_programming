#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last = -(-number % 10)
else:
    last = number % 10

greater = "and is greater than 5"
zero = "and is 0"
less = "and is less than 6 and not 0"

if last > 5:
    print(f"Last digit of {number} is {last} {greater}")
elif last == 0:
    print(f"Last digit of {number} is {last} {zero}")
else:
    print(f"Last digit of {number} is {last} {less}")

