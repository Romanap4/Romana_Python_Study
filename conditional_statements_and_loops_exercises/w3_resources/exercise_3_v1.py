# Write a Python program to guess a number between 1 and 9 --> version 1
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct
# On successful guess, user will get a "Well guessed!" message, and the program will exit.

import random

number = random.randint(1, 9)
guess = int(input("Enter your guess (1-9): "))
running = True

while running:
    if guess != number:
        guess = int(input("Your guess was not correct, please try again! Enter your guess (1-9): "))
    else:
        break
        
print("Well guessed!")
