# write a function to find the maximum of three numbers --> version 2

def maximum_number(a, b, c):
    if a > b and a > c:
        print(f"{a}")
    elif b > a and b > c:
        print(f"{b}")
    else:
        print(f"{c}")

maximum_number(1, 8, 3)
