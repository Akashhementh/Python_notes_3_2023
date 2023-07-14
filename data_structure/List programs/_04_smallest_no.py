print("-----------------To find the smallest number ------------------------------")
listA = []
listB = []
listC = []
n = int(input("Enter the length of the list"))
for i in range(0, n):
    print("enter the list {}".format(i+1))
    ele = input()
    listA.append(ele)
for i in listA:
    if str(i).isdigit():
        listB.append(i)
    else:
        listC.append(i)
print("there are the string values")
print(listC)
for i in range(0,len(listB)):
    for j in range(0,len(listB)):
        if listB[i] < listB[j]:
            listB[i], listB[j] = listB[j], listB[i]
print("smallest number is :", listB[0])


print("------------------------------------------2nd method------------------------------------------")

listA = [10, 34, 45, "apple"]
listB = []
listC = []
for i in range(0, len(listA)):
    if str(listA[i]).isdigit():
        listB.append(listA[i])
    else:
        listC.append(listA[i])
for i in range(0, len(listB)):
    for j in range(0, len(listB)):
        if listB[i] < listB[j]:
            listB[i], listB[j] = listB[j], listB[i]
print("smallest", listB[0])




