print("---------------------To find the largest number------------------------------------------------------")

listA = []
listB = []
listC = []
n = int(input("Enter the length"))
maximum = "0"
for i in range(n):
    print("Enter the number {}".format(i+1))
    ele = input()
    listA.append(ele)
for i in listA:
    if str(i).isdigit():
        listB.append(i)
    else:
        listC.append(i)
print("There is an string in the list or blank")
print("string", listC)
for i in listB:
    if i > maximum:
        maximum = i
print("the maximum element is:", maximum)



list1 = [10, 34, 4, "apple", "grapes", 68, "die"]
listB = []
listA = []
for i in range(0, len(list1)):
    if str(list1[i]).isdigit():
        listA.append(list1[i])
    else:
        listB.append(list1[i])
print("Integer numbers",listA)
print("non integer", listB)
for i in range(0, len(listA)):
    for j in range(0, len(listA)):
        if listA[i] > listA[j]:
            listA[i], listA[j] = listA[j], listA[i]
print("largest number :", listA[0])






