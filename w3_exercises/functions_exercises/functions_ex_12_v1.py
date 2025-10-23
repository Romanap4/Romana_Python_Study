# write a function that checks whether a passed string is a palindrome or not --> version 1

string = input("Enter a desired string: ")

def check_if_palindrome():
    if string == string[::-1]:
        print("This string is a palindrome")
    else:
        print("This string is not a palindrome")

check_if_palindrome()
