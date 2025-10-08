import random                               # importing random module

# print(help(random))

# low = 1
# high = 100
# options = ("rock", "paper", "scissors")
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# number = random.randint(1, 20)                     # d20 dice roll
# number = random.randint(low, high)                 # variables can be placed, as long as they contain numbers
# number = random.random()                           # use if you need a floating point number; this returns a number between 0 and 1
# print(number)

# option = random.choice(options)                    # use to pick a random choice in a sequence
# print(option)                                      # great choice for games if you need a random element

# random.shuffle(cards)
# print(cards)

# EXERCISE - number guessing

low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f"Enter a number between ({low} - {high}): "))
    guesses += 1

    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else:
        print(f"{guess} is correct")
        break

print(f"This round took you {guesses} guesses")

