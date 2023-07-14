listA = ['akash', 24, 'done']
listB = ['name', 'age', 'assignment']
my_dict ={}
for i in range(len(listA)):
    my_dict[listB[i]] = listA[i]
print(my_dict)
print("---------------------------------------------------------------------------------------------")
keys = ['name', 'age', 'city']
values = ['John', 25, 'New York']
my_dict = {k: v for k, v in zip(keys, values)}
print(my_dict)
