# Programming exercise: Countdown
# Counts down from the user's number to 1, then prints "Now!"

print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 0:
    print(number)
    number -= 1

print("Now!")
