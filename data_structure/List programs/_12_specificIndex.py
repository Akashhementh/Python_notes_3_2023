print("-----------------------remove specific index from list-----------------------------------")
listA = [12, 34, 56, 78, "apple", "grape", "dog", "cat", (2, 3, 4, 5), [12, 45, 34]]
listB = []
listC = []
print("Enter the index to be removed in listA", listA)
index = (input("Enter index number separated by comma"))
index1 = index.split(',')
for i in range(0, len(listA)):
    if str(i) in index1:
        listC.append(listA[i])
    else:
        listB.append(listA[i])
print("Remaining Element in the list", listB)
print("Removed elements:", listB)
