print("----------------------------Get unquie values-------------------------------------------")
listA = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 34, 5, 6, "apple", "apple"]
listB = []
for i in listA:
    if i not in listB:
        listB.append(i)
    else:
        continue
print("non unique values:", listB)
print("----------------------------Get unquie values-------------------------------------------")
listA = [1, [2, 2, 3], 3, 4, 5, 5, (1, 2, 3)]
listB = []
for i in listA:
    if isinstance(i, (list, tuple)):
        for j in i:
            if isinstance(j, (list, tuple)):
                listB.extend(j)
            else:
                listB.append(j)
    else:
        listB.append(i)
print(listB)
listC = []
listD = []
for char in listB:
    if char not in listC:
        listC.append(char)
    else:
        listD.append(char)
print("Unique Values in list are", listD)





