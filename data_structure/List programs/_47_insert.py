print("-------------------------Insert an element before each element of a list---------------------------")
listA = [10, 34, 56]
listB = []
for i in range(0, len(listA)):
        listB.append(i)
        listB.append(listA[i])
print("We are inserting index no:",listB)
print("----------------------------------------------------------------------------------------------")
listA = [10, 34, 56]
listB = []
element = "apple"
for i in range(0, len(listA)):
        listB.append(element)
        listB.append(listA[i])
print("We are inserting different no:", listB)
print("------------------------------------------------------------------------------------")
listA = [10, 34, 56]
listB = []
listC = [34, 56, 78]
for i in listA:
    for j in listC:
        listB.append(j)
    listB.append(i)
print("We are inserting different no:", listB)

