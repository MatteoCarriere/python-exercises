# Exercise: 2
# Task: Print the letter count of a word if it has more than one letter, then say thank you

num_word = input("Please type in a word: ")

word = len(num_word)

if word > 1:
    print(f"There are {word} letters in the word {num_word}")
    print("Thank you!")
if word <= 1:
    print("Thank you!")
