# Variables = A container for a value (string, integer, float, boolean)
#             A variable behaves as if it was the value it contains

#Strings
first_name = "Manyan"
food = "chocolate"
email = "bliblablu@faker.com"

print(f"Hello {first_name}")     #f means f-string --> easiest way to display a variable; f means "format"
print(f"You like {food}")
print(f"Your email is: {email}")

#Integers
age = 34
quantity = 3
num_of_students = 30

print(f"You are {age} years old.")
print(f"You are buying {quantity} items.")
print(f"Your class has {num_of_students} students.")

#Floats (floating point numbers)
price = 10.99
gpa = 3.2
distance = 9400.4

print(f"The price is ${price}.")
print(f"Your gpa is: {gpa}.")
print(f"You ran {distance}km.")

#Booleans  (a boolean is either true or false)
is_student = True       #or False
for_sale = True
is_online = True

print(f"Are you a student?: {is_student}")

if is_student:
    print("You are a student.")          #no need for f-string because we are not inserting variables in the string
else:
    print("You are NOT a student.")

if for_sale:
    print("That item is for sale.")
else:
    print("That item is not available.")

if is_online:
    print("You are online.")
else:
    print("You are offline.")
