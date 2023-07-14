print("-------------------------Printing elements in ascending order----------------------")
# listA = []
# n = int(input("Enter the length"))
# for i in range(0, n):
#     print("enter the element{}".format(i+1))
#     ele = input()
#     listA.append(ele)
listA = [12, 34, 5.6, "apple", [10, 49]]
listB = []
for i in listA:
    if isinstance(i, (int, float)):
        listB.append(i)
print("The number present in list", listB)
for i in range(0, len(listB)):
    for j in range(0, len(listB)):
        if listB[i] < listB[j]:
            listB[i], listB[j] = listB[j], listB[i]
print(listB[0])



