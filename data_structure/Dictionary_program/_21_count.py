# print("------------------Count the values associated with key in a dictionary-------------------")
# list_of_dicts = {'name': 'John', 'age': 25, 'city': 'New York',
#                  'nae': 'Alice', 'ge': 30, 'cty': 'London',
#                  'ne': 'Mike', 'e': 35, 'ci': 'Paris'}
# listA = []
# count = 0
# for keys, values in list_of_dicts.items():
#     listA.append(values)
# for i in listA:
#     count += 1
# print(count)

print("Convert a list into a nested dictionary of keys. ")
listA = ['akash', 34, 3.45]
nest_dict = []
for i in listA:
    if isinstance(i, int):
        nest_dict.append("{'num': " + str(i) + "}")
    if isinstance(i, str):
        nest_dict.append("{'name': '" + i + "'}")
out = "{" + ", ".join(nest_dict) + "}"
print(out)



