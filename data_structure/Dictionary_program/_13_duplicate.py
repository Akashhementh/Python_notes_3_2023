print("-------------------------------------Remove duplicates from Dictionary----------------------------------------")
my_dict = {'akash': 123, 'aman': 345, 'suma': 456, 'ai': 46, 'good': 'sr', 'aka': 123}
listA = {}
for i, j in my_dict.items():
    if j not in listA.values():
        listA[i] = j
my_dict = listA
print(my_dict)
print(listA)

