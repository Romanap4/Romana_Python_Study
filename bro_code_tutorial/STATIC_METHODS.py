# Static methods = A method that belongs to a class rather than any on+bject from that class (instance)
#                  Usually used for general utility functions

# Instance methods = Best for operation on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):                                              # instance method
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):                                 # static method
        valid_positions = ["Detective", "Social Media Admin", "Beekeeper", "Principal"]
        return position in valid_positions

employee1 = Employee("Wednesday", "Detective")
employee2 = Employee("Enid", "Social Media Admin")
employee3 = Employee("Eugene", "Beekeeper")

# output for static method; doesn't require an object, only the class
print(Employee.is_valid_position("Detective"))
print(Employee.is_valid_position("Cashier"))
# output for instance method; requires an object
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
