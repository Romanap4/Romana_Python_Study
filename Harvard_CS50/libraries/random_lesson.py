# import line of code brings the entire contents of the functions of a library, while from allows us to be very specific about what we'd like to import

from random import choice

coin = choice(["heads", "tails"])
print(coin)

# Instead of coding random.choice, this way we can code choice alone
# choice is then loaded explicitly into our program, allowing us to save system resources and potentially can make our code run faster
