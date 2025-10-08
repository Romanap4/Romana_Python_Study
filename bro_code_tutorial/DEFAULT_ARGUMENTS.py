# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

# def net_price(list_price, discount=0, tax=0.05):             # setting default arguments to make the function more flexible
#     return list_price * (1 - discount) * (1 + tax)           # also reduces the number of positional arguments

# print(net_price(500))
# print(net_price(500, 0.1, 0))                                # the function accepts up to two additional arguments; passed argument is used

# EXERCISE - making a countup timer

import time 

def count(end, start=0):                                        # default arguments should follow non-default arguments
    for x in range(start, end+1):                               # adding one because the second argument in range is exclusive  
        print(x)
        time.sleep(1)
    print("DONE!")

count(30, 15)                                                    # changed arguments


