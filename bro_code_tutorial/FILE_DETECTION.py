# Python file detection
# importing the os module provides a way for Python to interact with the operating system
# Relative file path = folder/test.txt
# Absolute file path = C:/Users/Romana/Desktop/test.txt

import os

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists.")
else:
    print("That location doesn't exist.")
