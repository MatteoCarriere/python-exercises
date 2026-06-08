# Exercise: 5
# Task: Ask for two numbers and an operation (add/multiply/subtract), then print the result

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
operation = input("Operation: ")

if operation == "add":
    print(f"{num1} + {num2} = {num1 + num2}")

if operation == "multiply":
    print(f"{num1} * {num2} = {num1 * num2}")

if operation == "subtract":
    print(f"{num1} - {num2} = {num1 - num2}")
