# Exercise: 4
# Task: Ask for two words and print which comes last alphabetically, or if they are the same
 
word1 = input("Please type in the 1st word: ")
word2 = input("Please type in the 2nd word: ")
 
if word1 > word2:
    print(f"{word1} comes alphabetically last.")
elif word1 == word2:
    print("You gave me the same word twice.")
else:
    print(f"{word2} comes alphabetically last.")
