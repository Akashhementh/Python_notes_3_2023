print("-----------create a dictionary from two lists without losing duplicate values.------------- ")
listA = [1, 7, 3, 4, 5]
listB = ['akki', 'akk', 'ak', 'ak', 'akk']
dictA = {}

for i, value in enumerate(listA):
    if isinstance(value, int):
        if value in dictA:
            dictA[value].append(listB[i])
        else:
            dictA[value] = [listB[i]]
print(dictA)


