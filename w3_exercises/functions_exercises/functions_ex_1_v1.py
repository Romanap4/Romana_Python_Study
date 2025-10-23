# write a function to find the maximum of three numbers --> version 1

def maximum_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
result = maximum_number(9, 3, 2)
print(result)
