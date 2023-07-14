listA = [1, [2, 3], [4, [5, 6]], 7]
listB = []
for i in listA:
    if isinstance(i, list):
        for j in i:
            if isinstance(j, list):
                listB.extend(j)
            else:
                listB.append(j)
    else:
        listB.append(i)
print(listB)

