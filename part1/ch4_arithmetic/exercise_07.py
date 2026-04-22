# Exercise: 7
# Task: Write a program which estimates a user's typical food expenditure

times_per_week = int(input("How many times a week do you eat at the student cafeteria?"))
typical_price = float(input("The price of a typical student lunch?"))
weekly_expense = float(input("How much money do you spend on groceries in a week?"))

cafeteria_cost = times_per_week * typical_price
weekly = cafeteria_cost + weekly_expense
daily = weekly / 7


print(f"Average food expenditure: ")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")