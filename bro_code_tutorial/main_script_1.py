# print(dir())

# you can think of an attribute as a variable
# dunder --> double underscore
# * --> means everything

# from main_script_2 import *
# print(__name__)

def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print("This is script1")
    favorite_food("chocolate")
    print("Goodbye!")

if __name__ == '__main__':
    main()
