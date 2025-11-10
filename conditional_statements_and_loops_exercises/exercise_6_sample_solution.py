# Write a Python program to count the number of even and odd numbers in a series of numbers
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4

# Create a tuple named 'numbers' containing integer values from 1 to 9
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Initialize counters for counting odd and even numbers
count_odd = 0
count_even = 0

# Iterate through each element 'x' in the tuple 'numbers'
for x in numbers:
    # Check if the current number 'x' is even by evaluating 'not x % 2'
    if not x % 2:  # If 'x' modulo 2 equals 0, it's even
        # Increment the count of even numbers
        count_even += 1
    else:
        # If 'x' modulo 2 doesn't equal 0, it's odd; increment the count of odd numbers
        count_odd += 1

# Print the total count of even and odd numbers
print("Number of even numbers:", count_even)
print("Number of odd numbers:", count_odd)
