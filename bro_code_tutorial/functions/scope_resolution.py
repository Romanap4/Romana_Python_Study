# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB rule) Local -> Enclosed -> Global -> Built-In

# LOCAL SCOPE
# variables declared within a function have a local scope
# functions can't "see" inside of other functions; that's why we pass arguments to functions, so that they would be "aware" of them
# def func1():
#     a = 1
#     print(a)

# def func2():
#     b = 2
#     print(b)

# func1()
# func2()

# it's possible to create different versions of the same variable:

# def func1():
#     x = 2
#     print(x)

# def func2():
#     x = 2
#     print(x)

# ENCLOSED SCOPE
# order of operations - use local variables first, and then enclosed
# if the local scope is eliminated (x = 2), the enclosed scope is used (x = 1)

# def func1():
#     x = 1

#     def func2():
#         x = 2
#         print(x)
#     func2()

# func1()

# GLOBAL SCOPE  --> outside of any functions
# if there is no local or enclosed version, global version is used

# def func1():
#     print(x)

# def func2():
#     print(x)

# x = 3

# func1()
# func2()

# BUILT-IN
# variables can share the same name as long as they're within a different scope
from math import e

def func1():
    print(e)

e = 3

func1()
