# Exercise: 1
# Task: Print a different message based on age: too young to write, normal, or impossible age
 
age = int(input("What is your age? "))
 
if age >= 5:
    print(f"Ok, you're {age} years old")
elif age >= 0 and age < 5:
    print(f"I suspect you can't write quite yet...")
elif age < 0:
    print("That must be a mistake")
