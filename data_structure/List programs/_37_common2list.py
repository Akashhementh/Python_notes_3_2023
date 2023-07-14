print("-------------------------Finding common items from two lists---------------------------------")
listA = [23, 45, "apple", 34.56, [23, 45]]
listB = [13, 5, "lion", 34.56, 45, [23, 45]]
listC = []
for i in listA:
    for j in listB:
        if i == j:
            listC.append(i)
print(listC)
print("----------------------------------------------------------------------------------------------")
listA = []
n = int(input("Enter the length of the list-A"))
for i in range(0, n):
    print("enter the element{}".format(i+1))
    ele = input()
    listA.append(ele)
listB = []
n = int(input("Enter the length of the list-B"))
for i in range(0, n):
    print("enter the element{}".format(i+1))
    ele = input()
    listB.append(ele)
print(listA)
print(listB)
listC = []
for i in listA:
    for j in listB:
        if i == j:
            listC.append(i)
print("The common Element in the List", listC)