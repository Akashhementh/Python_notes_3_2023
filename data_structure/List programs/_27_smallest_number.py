print("--------------------------------------Finding a second smallest number-----------------------------")
listA = []
n = int(input("Enter the length of the list"))
for i in range(0, n):
    print("Enter the Element{}".format(i+1))
    ele = input()
    listA.append(ele)
listB = []
for i in listA:
    if str(i).isdigit():
        listB.append(i)
for i in range(0, len(listB)):
    for j in range(0, len(listB)):
        if listB[i] < listB[j]:
            listB[i], listB[j] = listB[j], listB[i]
print(listB[1])