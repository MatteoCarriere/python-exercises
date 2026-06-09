# Exercise: 4
# Task: Print FizzBuzz if divisible by both 3 and 5, Fizz by 3, Buzz by 5
 
number = int(input("Number: "))
 
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
