# Exercise: 6
# Task: Convert Fahrenheit to Celsius and print a "brr" message if below freezing

tempF = int(input("Please type in a temperature (F): "))

tempC = (tempF - 32) * 5/9
print(f"{tempF} degrees Fahrenheit equals {tempC} degrees Celsius")

if tempC < 0:
    print(f"Brr! It's cold in here!")
