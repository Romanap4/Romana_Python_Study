# write a function to check whether a number is "Perfect" or not

number_to_check = int(input("Enter a number to check: "))

# positive divisors sum = number 
# (positive divisors + number) / 2 = number 

# def is_number_perfect():

#     x = 0

#     for divisor in range(1, number_to_check + 1):
#         if number_to_check % divisor == 0:
#             x += divisor
    
#     sum_of_divisors = divisor + sum_of_divisors
     

#     if number_to_check == sum_of_divisors and (sum_of_divisors + number_to_check) / 2 == number_to_check:
#         print("This is a perfect number")
#     else:
#         print("This is not a perfect number")

# is_number_perfect()

# Define a function named 'perfect_number' that checks if a number 'n' is a perfect number
def perfect_number(n):
    # Initialize a variable 'sum' to store the sum of factors of 'n'
    sum = 0
    
    # Iterate through numbers from 1 to 'n-1' using 'x' as the iterator
    for x in range(1, n):
        # Check if 'x' is a factor of 'n' (divides 'n' without remainder)
        if n % x == 0:
            # If 'x' is a factor of 'n', add it to the 'sum'
            sum += x
    
    # Check if the 'sum' of factors is equal to the original number 'n'
    return sum == n

# Print the result of checking if 6 is a perfect number by calling the 'perfect_number' function
print(perfect_number(6)) 
