import os

file_path = "test.txt"

if os.access(file_path, os.R_OK):
    print(f"The file '{file_path}' is readable.")
else:
    print(f"The file '{file_path}' is not readable.")

if os.access(file_path, os.W_OK):
    print(f"The file '{file_path}' is writable.")
else:
    print(f"The file '{file_path}' is not writable.")

if os.access(file_path, os.X_OK):
    print(f"The file '{file_path}' is executable.")
else:
    print(f"The file '{file_path}' is not executable.")
