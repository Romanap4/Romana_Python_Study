# STRIP METHOD - removes any whitespace from the left and the right side of the user input
# use rstrip() and lstrip() to clear the right or the left side of the user input respectively
# TITLE METHOD - title cases the user's input

# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the string
name = name.strip()

# Capitalize the first letter of each word
name = name.title()

# Print the output
print(f"Hello, {name}")

# STACKING METHODS - a few methods can be stacked for efficiency

# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the string and capitalize the first letter of each word
name = name.strip().title()

# Print the output
print(f"Hello, {name}")

# Shortening the code further

# Ask the user for their name, remove whitespace from the string and capitalize the first letter of each word
name = input("What's your name? ").strip().title()

# Print the output
print(f"Hello, {name}")
