# Variables = A reusable container for a value (string, integer, float, boolean)
#             A variable behaves as if it was the value it contains
#             Each variable should have a unique name

# +++++++ STRINGS +++++++
first_name = "Manyan"            # "=" --> assignment operator; use to assign a variable
food = "chocolate"
email = "bliblablu@faker.com"

print(f"Hello {first_name}")
#f means f-string --> easiest way to display a variable; f means "format" (this is string interpolation)
# string interpolation is used to insert a variable into a string; use {}
print(f"You like {food}")
print(f"Your email is: {email}")

# +++++++ INTEGERS +++++++
# a whole number; don't put it between quotes, as that would make it a string
# integers can be used in arithmetic expressions; if they were strings, that wouldn't be possible
age = 34
quantity = 3
num_of_students = 30

print(f"You are {age} years old.")
print(f"You are buying {quantity} items.")
print(f"Your class has {num_of_students} students.")

# ++++++++ FLOATS +++++++
# (floating point numbers); a number with a decimal portion
price = 10.99
gpa = 3.2
distance = 9400.4

print(f"The price is ${price}.")
print(f"Your gpa is: {gpa}.")
print(f"You ran {distance}km.")

# +++++++ BOOLEANS +++++++ 
# (a boolean is either True or False)
# boolean values are not outputed directly, but more likely used internally within a program (if statements for example)
is_student = True
for_sale = False
is_online = True

print(f"Are you a student?: {is_student}")

#no need for f-string because we are not inserting variables in the string (not using string interpolation)
if is_student:
    print("You are a student.")
else:
    print("You are NOT a student.")

if for_sale:
    print("That item is for sale.")
else:
    print("That item is NOT available.")

if is_online:
    print("You are online.")
else:
    print("You are offline.")
