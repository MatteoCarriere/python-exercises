# Project: Number guessing game
# The computer picks a secret number from 1 to 100 and the player
# guesses until they find it, getting "higher"/"lower" hints.
# Difficulty sets how many attempts the player has.

import random

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")

play_again = "y"
games_won = 0
games_played = 0

while play_again == "y":
    print()
    print("Choose difficulty: easy (10 tries), medium (7), hard (5)")
    difficulty = input("Difficulty: ")
    if difficulty == "easy":
        max_attempts = 10
    elif difficulty == "hard":
        max_attempts = 5
    else:
        max_attempts = 7
        print("Medium it is.")

    secret = random.randint(1, 100)
    attempts = 0
    won = False

    while attempts < max_attempts:
        text = input(f"Guess ({max_attempts - attempts} left): ")
        # isdigit() is True only if the text is made of digits,
        # so typing "abc" doesn't crash the program
        if not text.isdigit():
            print("Please type a whole number.")
            continue
        guess = int(text)
        if guess < 1 or guess > 100:
            print("The number is between 1 and 100.")
            continue

        attempts += 1
        if guess < secret:
            print("Higher!")
        elif guess > secret:
            print("Lower!")
        else:
            won = True
            break

    games_played += 1
    if won:
        games_won += 1
        print(f"Correct! The number was {secret}. You needed {attempts} attempts.")
    else:
        print(f"Out of attempts! The number was {secret}.")

    print(f"Score: {games_won} won out of {games_played}")
    play_again = input("Play again? (y/n): ")

print("Thanks for playing!")
