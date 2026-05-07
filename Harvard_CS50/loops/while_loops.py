while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break

# The continue statement explicitly tells PYthon to go to the next iteration of a loop
# The break statement tells Python to "break out" of a loop early, before it has finished all of its iterations

# The continue statement is redundant

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

# Improving the code using functions; using the return statement to return the value of n back to the main function
# Functions can be called within other functions

def main():
    meow(get_number())

def get_number():
    n = int(input("What's n? "))
    if n > 0:
        return n
    
def meow():
    for _ in range(n):
        print("meow")

main()
