# Exercise: 2
# Task: If the integer is less than 0 it gets multiplied by -1

num = int(input("Please type in a number: "))

if num < 0:
    print(f"The absolute value of this number is {num * -1}")

if num >= 0:
    print(f"The absolute value of this number is {num}")