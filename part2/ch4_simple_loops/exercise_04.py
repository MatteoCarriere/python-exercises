# Exercise: 4
# Task: Ask for a password, then keep asking to repeat it until they match
 
password = input("Password: ")
 
while True:
    repeated_password = input("Repeat password: ")
    if repeated_password == password:
        print("User account created!")
        break
    else:
        print("They do not match!")
