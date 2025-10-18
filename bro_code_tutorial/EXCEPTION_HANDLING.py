# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1. try, 2. except, 3. finally

# ZeroDivisionError --> attempting to divide by zero
# 1 / 0

# TypeError --> attempting to perform an operation of a value that's the wrong data type
# 1 + "1"

# ValueError --> attempting to typecast a value of the wrong data type
# int("pizza")

# try:
# Try some code
# except Exception:
# handle an Exception
# finally:
# Do some clean up

# this code is considered dangerous because the user can type in anythig; surround it within a try block
try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero IDIOT!")
except ValueError:
   print("Enter only numbers please!")
# bad practice, it will catch all exceptions, but it's too broad of a clause
except Exception:
    print("Something went wrong!")
# the finally block always executes, regardless if there's an exception or not
finally:
    print("Do some cleanup here")
