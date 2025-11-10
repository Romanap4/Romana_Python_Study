# Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and 
# for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".

for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)
