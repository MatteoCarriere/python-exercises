# Exercise: 4
# Task: Print which thresholds (1000, 100, 10) the number is smaller than, then say thank you

num = int(input("Please type in a number: "))

if num < 1000:
    print(f"This number is smaller than 1000")

if num < 100:
    print(f"This number is smaller than 100")

if num < 10:
    print(f"This number is smaller than 10")

print(f"Thank you!")
