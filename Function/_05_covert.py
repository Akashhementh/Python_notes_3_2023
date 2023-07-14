print("---------convert list/tuple/set to list/tuple/set--------------------------------------------------------")
def list_to_tuple(input):
    return tuple(input)
def list_to_set(input):
    return set(input)
def tuple_to_list(input):
    return list(input)
def tuple_to_set(input):
    return set(input)
def set_to_list(input):
    return list(input)
def set_to_tuple(input):
    return tuple(input)

listA = [1, 2, 3, 4, 5]
my_tuple = list_to_tuple(listA)
my_set = list_to_set(listA)

print(my_tuple)
print(my_set)

tupleA = (1, 2, 3, 4, 5, 6, 7)
my_list = tuple_to_list(tupleA)
my_set = tuple_to_set(tupleA)

print(my_list)
print(my_set)

setA = {1, 2, 3, 4, 5, 6}
my_list = set_to_list(setA)
my_tuple = set_to_tuple(setA)

print(my_list)
print(my_tuple)
