# Exercise: 3
# Task: If the name is anything but "Jerry", it prints out the total cost

name = (input("Please tell me your name: "))

if name != 'Jerry':
    num_soup =  int(input("How many portions of soup? "))
    print(f"The total cost is {num_soup * 5.90}")
    print(f"Next please!")

# If is Jerry it only says "Next please!"
print(f"Next please!")