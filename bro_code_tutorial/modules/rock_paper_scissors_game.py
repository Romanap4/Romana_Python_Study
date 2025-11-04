# Rock, paper, scissors game in Python

import random

# we are not going to be changing the option, so a tuple is a better choice, since it's faster
options = ("rock", "paper", "scissors")
running = True
# using a boolean variable to make it easier to find the break statement by highlighting the variable

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    # play_again = input("Play again? (y/n): ").lower()
    # if not play_again == "y":
    #     running = False
    # to avoid creating another variable, there is another way:

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")
