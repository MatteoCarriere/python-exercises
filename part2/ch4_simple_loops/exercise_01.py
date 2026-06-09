# Exercise: 1
# Task: Print "hi" in a loop until the user types "no"
 
while True:
    print("hi")
    question = input("Shall we continue? ")
    if question == "no":
        break
print("okay then")
