import random
# importing the random module; it gives us access to a lot of useful methods involving random numbers

# HELP FUNCTION --> use the help function to get a comprehensive list of the methods within the module
# print(help(random))

# low = 1
# high = 100
# options = ("rock", "paper", "scissors")
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# D20 DICE ROLL; getting a random whole integer from a range; the last number is inclusive
# number = random.randint(1, 20)
# USING VARIABLES --> variables can be placed within the randint method, as long as they contain numbers
# number = random.randint(low, high)
# GETTING A FLOATING POINT NUMBER --> use the random method if you need a floating point number; this returns a number between 0 and 1
# number = random.random()

# print(number)

# CHOICE METHOD --> use to pick a random choice in a sequence; it's a great choice for games that require a random element
# option = random.choice(options)
# print(option)

# SHUFFLE METHOD --> use to shuffle a collection of options
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
