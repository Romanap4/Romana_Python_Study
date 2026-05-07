# Implement a function called `convert` that accepts a `str` as input and returns that same input with any `:)` converted to 🙂 and any `:(` converted to 🙁. All other text should be returned unchanged.
# Then, in that same file, implement a function called `main` that prompts the user for input, calls `convert` on that input, and prints the result.  

def main():
    string = input("Enter your sentence here: ")
    convert(string)
    print(string)

def convert(string):
    string = string.replace(":)", "🙂")
    string = string.replace(":(", "🙁")
    return string

main()

# I'll be back!
