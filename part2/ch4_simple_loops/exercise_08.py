# Programming exercise: Working with numbers
# Reads integers until the user enters 0, then prints
# count, sum, mean, and counts of positive/negative numbers.

print("Please type in integer numbers. Type in 0 to finish.")
numbers = 0
total = 0
mean = 0
positives = 0
negatives = 0

while True:
    number = int(input("Number: "))
    if number == 0:
        break
    numbers += 1
    total += number
    mean = total / numbers
    if number > 0:
        positives += 1
    else:
        negatives += 1

print(f"Numbers typed in {numbers}")
print(f"The sum of the numbers is {total}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positives}")
print(f"Negative numbers {negatives}")
