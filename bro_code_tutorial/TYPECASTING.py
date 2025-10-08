# typecasting = The process of converting a value of one data type to another 
#               (string, integer, float, boolean)
#               Explicit vs Implicit

# Explicit typecasting - manually converting a value or variable into a different data type by using one of the cast keywords
name = "Manyan"
age = 34
gpa = 1.9
student = True

print(type(name))     # built-in type function --> shows the data type of a variable
print(type(age))
print(type(gpa))
print(type(student))

age = float(age)
print(age)
print(type(age))

gpa = int(gpa)
print(gpa)
print(type(gpa))

student = str(student)
print(student)
print(type(student))

age = bool(age)   # when converting a number to a boolean, if the number is anything but zero, it's always going to be true
print(age)

name = bool(name)
print(name)

# Implicit typecasting - a value or a variable is converted into a different data type automatically
x = 2
y = 2.0

x = x / y

print(x)   # x became a float; 
           # a variable's data type can be converted when you perform certain operations on it (such as arithemtic)