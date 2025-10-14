# Nested class = A class defined while within another class
#                class Outer:
#                   class Inner:

# Benefits: Allows you to logically group classes that are closely related
#           Encapsulates private details that aren't relevant outside of the outer class
#           Kepps the namespace clean; reduces the possibility of naming conflicts

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]

company1 = Company("Nevermore")
company2 = Company("JYP Entertainment")

company1.add_employee("Wednesday", "Detective")
company1.add_employee("Enid", "Social Media Admin")
company1.add_employee("Eugene", "Beekeeper")

company2.add_employee("JY Park", "CEO")
company2.add_employee("Bang Christopher Chan", "Producer, singer")
company2.add_employee("Seo Changbin", "Producer, rapper")

for employee in company1.list_employees():
    print(employee)

for employee in company2.list_employees():
    print(employee)

# print(company.list_employees())

#         print("This is the first class.")

# class Nonprofit:
#     class Employee:
#         print("This is the second class.")
