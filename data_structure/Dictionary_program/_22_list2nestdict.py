# print("--------------------------Convert a list into a nested dictionary of keys. ---------------------------")
# listA = ['akash', 34, 3.45]
# nest_dict = []
# for i in listA:
#     if isinstance(i, int):
#         nest_dict.append("{'num': " + str(i) + "}")
#     if isinstance(i, str):
#         nest_dict.append("{'name': '" + i + "'}")
# output = "{" + ", ".join(nest_dict) + "}"
# print(output)
#
# print("--------------------------Sort a list alphabetically in a dictionary.------------------------------")
# my_dict = {'fruit': ['orange', 'apple', 'bananna', 'grapes'], 'animal': ['lion', 'monkey', 'Donkey', 'goat']}
# sorted_dict = {keys: sorted(values) for keys, values in my_dict.items()}
# print(sorted_dict)

my_dict = {'fruit': 'apple', 'find': 56, 45: 'akdk'}
sorted_dict = {keys: sorted(values)for keys, values in my_dict.items()}
print(sorted_dict)


