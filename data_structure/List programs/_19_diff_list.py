
print("-----------------------------------difference between two list---------------------------------")
listA = []
n = int(input("Enter the length :"))
for i in range(0, n):
    print("enter the listA element{}".format(i+1))
    ele = input()
    listA.append(ele)
listB = []
print("List-A", listA)
m = int(input("Enter the length"))
for i in range(0, m):
    print("enter the listB element{}".format(i+1))
    elm = input()
    listB.append(elm)
listC = []
for char in listA:
    if char not in listB:
        listC.append(char)
for value in listB:
    if value not in listA:
        listC.append(value)
print("Difference between two list", listC)

print("------------------------------------------------------------------------------------------------------------")
listA = [12, 34, "tiger", (4, 4, 10), [34, "lion"]]
listB = [12, 78, (4, 4, 9)]
listC = []
for i in listA:
    if i not in listB:
        listC.append(i)
for j in listB:
    if j not in listA:
        listC.append(j)
print("difference Between list", listC)

print("------------------------------------------------------------------------------------------------------------")
listA = [100, 23, 48, "apple",[10, 50], 45, 67]
listC = []
listB = [45, 56, 78,"lion", (30, 40)]
listD = []
for i in listA:
    if str(i).isdigit():
        listC.append(i)
for i in listB:
    if str(i).isdigit():
        listD.append(i)
list1 = []
print("The integer present in both the list", listC, listD)
for char in range(0, len(listC)):
    for value in range(0, len(listD)):
        if char == value:
            ele = listC[char] - listD[value]
            list1.append(ele)
print("The difference between the elements", list1)

