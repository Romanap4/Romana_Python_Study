# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):                     # instance variables inside the constructor   
        self.name = name
        self.age = age
        Student.num_students += 1

# any code written within the constructor will always be executed when we instantiate an object

student1 = Student("Wednesday", 16)
student2 = Student("Enid", 15)
student3 = Student("Manyan", 34)
student4 = Student("Seo", 25)

print(student2.name)
print(student2.age)
print(Student.class_year)

# it's good practice to access the class variable using the name of the class, rather than the name of an object created from
# that class

# class variables:

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")

# instance variables:

print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
