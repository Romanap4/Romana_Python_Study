# typecasting = The process of converting a value of one data type to another
#               (string, integer, float, boolean)
#               Explicit vs Implicit

# +++++++++++ EXPLICIT TYPECASTING +++++++++++ 
# manually converting a value or variable into a different data type by using one of the cast keywords
name = "Manyan"
age = 34
gpa = 1.9
student = True

# built-in type function --> shows the data type of a variable
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

age = float(age)
print(age)
print(type(age))

# the decimal point will get truncated because it can't be contained
gpa = int(gpa)
print(gpa)
print(type(gpa))

# the result will appear the same, but it will be treated as a series of characters (string), rather than a boolean value
student = str(student)
print(student)
print(type(student))

# when converting a number to a boolean, if the number is anything but zero, it's always going to be True
age = bool(age)
print(age)

# typecasting to a boolean can be useful to check if a user entered some input; in case of an empty string, it will return as False
name = bool(name)
print(name)

# +++++++++++ IMPLICIT TYPECASTING +++++++++++++
# a value or a variable is converted into a different data type automatically
x = 2
y = 2.0

x = x / y

print(x)   
# x became a float;
# a variable's data type can be converted when you perform certain operations on it (such as arithemtic)
