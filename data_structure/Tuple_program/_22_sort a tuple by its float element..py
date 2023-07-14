print("------------sort a tuple by its float element.----------------------------")
my_tuple = (("apple", 2.5), ("banana", 1.8), ("cherry", 3.2))
sorted_tuple = sorted(my_tuple, key=lambda x: x[1])
print("Sorted Tuple:", sorted_tuple)


