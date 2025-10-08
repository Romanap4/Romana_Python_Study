# if = do some code only IF some condition is True
#      Else do something Else

#age = int(input("Enter your age: "))       # be careful with the order of the statements

#if age >= 100:
#    print("You are too old to sign up")
#elif age >= 18:
#    print("You are now signed up")
#elif age < 0:
#    print("You haven't been born yet")
#else:
#    print("You must be 18+ to sign up")  

#response = input("Would you like food? (Y/N): ")

#if response == "Y":                          # use == to check if two values are equal, comparison operator
#    print("Have some food!")                 # = is the assignment operator 
#else:
#    print("No food for you!")

#name = input("Enter your name: ")

#if name == "":
#    print("You did not type in your name!")
#else:
#    print(f"Hello {name}")

# using booleans with if statements

for_sale = True

if for_sale:                                   # a boolean variable can be used in place of a condition
    print("This item is for sale")             # condition would evaluate to be true or false
else:
    print("This item is NOT for sale")    

online = True

if online:
    print("The user is online")
else:
    print("The user is offline")

