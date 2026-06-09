# Exercise: 2
# Task: Ask for two numbers and print which one is greater, or if they are equal
 
num1 = int(input("Please type in the first number: "))
num2 = int(input("Please type in another number: "))
 
if num1 > num2:
    print(f"The greater number was : {num1}")
elif num2 > num1:
    print(f"The greater number was: {num2}")
elif num1 == num2:
    print(f"The numbers are equal!")
