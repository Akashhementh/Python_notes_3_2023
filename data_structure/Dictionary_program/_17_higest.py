print("-----Find the highest 3 values in a dictionary.---")
my_dict = {'akash': 123, 'aman': 345, 'suma': 456, 'ai': 456, 'good': 'sr', 'aka': 123}
listA = []
listB = []
for keys, values in my_dict.items():
    listA.append(values)
print(listA)
for i in listA:
    if isinstance(i, int):
        listB.append(i)
        for i in range(0, len(listB)):
            for j in range(0, len(listB)):
                if listB[i] > listB[j]:
                    listB[i], listB[j] = listB[j], listB[i]
g_dict = []
higest = listB[:3]
for keys1, values2 in my_dict.items():
    if values2 in higest:
        g_dict.append([keys1, values2])
print(g_dict)






