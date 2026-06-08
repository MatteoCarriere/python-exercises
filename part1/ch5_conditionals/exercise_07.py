# Exercise: 7
# Task: Calculate daily wages and double the pay if the day is Sunday

hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
days_of_the_week = input("Day of the week: ")

daily_wages = hourly_wage * hours_worked

if days_of_the_week == "Sunday": 
    print(f"Daily wages: {daily_wages * 2} euros")

if days_of_the_week != "Sunday":
    print(f"Daily wages: {daily_wages} euros")
