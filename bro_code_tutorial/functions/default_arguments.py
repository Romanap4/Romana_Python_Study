# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted when you invoke a function
#                     make your functions more flexible, reduces # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

# use default arguments when they are consistent most of the time
# setting default arguments to make the function more flexible
# it also reduces the number of positional arguments
# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500))
# the function accepts up to two additional arguments; the arguments that are passed will be used
# print(net_price(500, 0.1, 0))

# EXERCISE - making a countup timer

import time

# default arguments should follow positional (non-default) arguments
def count(end, start=0):
# adding one because the second argument in range is exclusive
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

# changed arguments are used
count(30, 15)
