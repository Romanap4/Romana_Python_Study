# write a program to print the even numbers from a given list --> version 1

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_numbers():
    even_numbers_list = []

    for even_number in sample_list:
        if even_number % 2 == 0:
            even_numbers_list.append(even_number)

    print(even_numbers_list)

even_numbers()
