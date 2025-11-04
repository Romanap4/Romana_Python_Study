import random
import string
# importing the string module

# importing the punctuation constant, the digits constant, and the ascii_letters constant:
chars = " " + string.punctuation + string.digits + string.ascii_letters
# string.whitespace --> adds spaces; includes things like carriage return and would warp the results
chars = list(chars)
# typecasting as a list where each character is an individual element
key = chars.copy()
# creating a copy of the list to serve as a key; the key will be shuffled

random.shuffle(key)

print(f"chars: {chars}")
print(f"key:   {key}")

# ENCRYPT

# original message --> plain_text
# encrypted message --> cipher_text

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

# DECRYPT

cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message: {plain_text}")
