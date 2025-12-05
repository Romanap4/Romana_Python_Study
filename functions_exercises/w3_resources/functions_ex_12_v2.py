# write a function that checks whether a passed string is a palindrome or not --> version 1

string = input("Enter a string you wish to check: ")

def check_if_palindrome():
    if string == string[::-1]:
        return "This string is a palindrome"
    else:
        return "This string is not a palindrome"
    
print(check_if_palindrome())
