# Exercise: 6
# Task: Given a year, find and print the next leap year after it
 
year = int(input("Year: "))
original = year
year = year + 1
 
while True:
    if year % 400 == 0:
        print(f"The next leap year after {original} is {year}")
        break
    elif year % 100 == 0:
        year = year + 1
    elif year % 4 == 0:
        print(f"The next leap year after {original} is {year}")
        break
    else:
        year = year + 1
