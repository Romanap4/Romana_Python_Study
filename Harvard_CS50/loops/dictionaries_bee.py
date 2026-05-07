WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

# def main():
#     print("Welcome to Spelling Bee!")
#     print("Your letters are: A I P C R H G")

#     while len(WORDS) > 0:
#         print(f"{len(WORDS)} words left!")
#         guess = input("Guess a word: ")

#         # TODO: Check if guess in dictionary
#         if guess == "GRAPHIC":
#             WORDS.clear()
#             print("You've won!")
#         if guess in WORDS.keys():
#             points = WORDS.pop(guess)
#             print(f"Good job! You scored {points} points.")

#     print("That's the game!")

# main()

# POP METHOD will return the value associated with a key and remove that key from the dictionary.

# Iterating over the whole dictionary to just show all the possible words and the number of points:

def main():
    print("Welcome to Spelling Bee!")
    for word, points in WORDS.items():
        print(f"{word} was worth {points} points.")

main()

# You can write "key, value" instead of "word, points"
