# write a function that accepts a string and counts the number of upper and lower case letters --> version 2

string = input("Enter a string to check the number of lowercase and uppercase letters: ")

def sum_lower_upper():

    def sum_lower():
        print(f"The number of lowercase letters is: {sum(lower.islower() for lower in string)}")

    def sum_upper():
        print(f"The number of uppercase letters is: {sum(upper.isupper() for upper in string)}")

    lower = sum_lower()
    upper = sum_upper()

sum_lower_upper()
