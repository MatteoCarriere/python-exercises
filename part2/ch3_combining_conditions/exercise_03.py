# Exercise: 3
# Task: Convert a points score [0-100] into a grade from fail to 5, rejecting out-of-range values
 
points = int(input("How many points [0-100]: "))
 
if points < 0:
    print("Grade: impossible!")
elif points >= 0 and points <= 49:
    print("Grade: fail")
elif points >= 50 and points <= 59:
    print("Grade: 1")
elif points >= 60 and points <= 69:
    print("Grade: 2")
elif points >= 70 and points <= 79:
    print("Grade: 3")
elif points >= 80 and points <= 89:
    print("Grade: 4")
elif points >= 90 and points <= 100:
    print("Grade: 5")
elif points > 100:
    print("Grade: impossible!")
 