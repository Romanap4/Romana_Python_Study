# Implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer. 

m = int(input("Enter the mass in kilograms: "))
c = 300000000

E = m * c**2

print(f"Energy is {E} J")
