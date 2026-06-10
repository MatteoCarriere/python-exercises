# Exercise: 7
# Task: Collect words into a story until the user types "end" or repeats a word twice in a row
 
words = ""
previous = ""
 
while True:
    word = input("Please type in a word: ")
    
    if word == "end":
        break
    elif word == previous:
        break
    
    previous = word
 
    if words == "":
        words += word
    else:
        words += " " + word
 
print(words)
 