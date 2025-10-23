# write a function that takes a list and returns a new list with distinct elements from the first list --> version 1

sample_list = [1,2,3,3,3,3,4,5]

def unique_list():
    unique_set = set(sample_list)
    return list(unique_set)

print(unique_list())
