# write a function that accepts a string and counts the number of upper and lower case letters --> version 1
# SUM EXISTS!

string = input("Enter a string to check the number of lowercase and uppercase letters: ")

def sum_lower_upper():

    def sum_lower():
        return f"The number of lowercase letters is: {sum(lower.islower() for lower in string)}"

    def sum_upper():
        return f"The number of uppercase letters is: {sum(upper.isupper() for upper in string)}"

    print(sum_lower())
    print(sum_upper())

sum_lower_upper()
