# In a series of if statements, each if statement is evaluated in order
# The flow of decisions is called "control flow"

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

# By using elif statements instead of if statements, we are asking fewer questions
# The program will stop when it finds a statement to be True and will not evaluate the rest of the elif statements

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

# You can also use the default, "catch-all" else statement to further decrease complexity

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
