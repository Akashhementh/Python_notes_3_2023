# print("------------------------------Sort a list of nested dictionaries----------------------------------")
# listA = [{'a': 234}, {'b': 456}, {'d': 784}]
# for i in range(len(listA)-1):
#     for j in range(len(listA)-1-i):
#         if listA[j] > listA[j+1]:
#             listA[i], listA[j+1] = listA[i], listA[j+1]
# print(listA)
print("------------------------------Sort a list of nested dictionaries----------------------------------")
listA = [{'a': 234}, {'b': 456}, {'d': 784}]

for i in range(len(listA) - 1):
    for j in range(len(listA) - 1 - i):
        if j > j + 1:
            listA[j], listA[j + 1] = listA[j + 1], listA[j]

print(listA)