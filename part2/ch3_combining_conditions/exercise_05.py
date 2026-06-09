# Exercise: 5
# Task: Determine if a year is a leap year using the 400/100/4 divisibility rules
 
leap_year = int(input("Please type in a year: "))
 
if leap_year % 400 == 0:
    print("That year is a leap year")
elif leap_year % 100 == 0:
    print("That year is not a leap year")
elif leap_year % 4 == 0:
    print("That year is a leap year")
else:
    print("That year is not a leap year.")
