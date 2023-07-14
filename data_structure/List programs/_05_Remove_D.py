print("---------------------------remove Duplicates------------------------")
listA = [10,20,49,"apple", "Bannana", 56,20,49,[10,20]]
listB = []
listC = []
for i in range(0, len(listA)):
    if listA[i] in listB:
        continue
    else:
        listC.append(listA[i])
        listB.append(listA[i])
print("after removing Duplicates", listC)


print("-------------------2nd method----------------------------------------")
listA = []
listB = []
listC = []
n = int(input("Enter the length of the list"))
for i in range(0, n):
    print("Enter the list{}".format(i+1))
    ele = input()
    listA.append(ele)
for i in range(0, len(listA)):
    if listA[i] in listB:
        continue
    else:
        listC.append(listA[i])
        listB.append(listA[i])
print("after removing Duplicates", listC)



