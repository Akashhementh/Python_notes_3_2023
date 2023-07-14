print("----------------------Get the maximum and minimum value in a dictionary.----------------------------------")
my_dict = {'akash': 123, 'aman': 345, 'suma': 456, 'akki': 46, 'good': 'sr'}
min_value = None
max_value = None
for i in my_dict.values():
    if isinstance(i, int):
        if (min_value is None) or (min_value > i):
            min_value = i
        if (max_value is None) or (max_value < i):
            max_value = i
print(min_value)
print(max_value)



