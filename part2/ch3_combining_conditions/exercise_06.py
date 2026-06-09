# Exercise: 6
# Task: Ask for three letters and print which one comes in the middle alphabetically
 
letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")
 
if letter1 >= letter2 and letter1 <= letter3:
    print("The letter in the middle is", letter1)
elif letter1 >= letter3 and letter1 <= letter2:
    print("The letter in the middle is", letter1)
elif letter2 >= letter1 and letter2 <= letter3:
    print("The letter in the middle is", letter2)
elif letter2 >= letter3 and letter2 <= letter1:
    print("The letter in the middle is", letter2)
else:
    print("The letter in the middle is", letter3)
