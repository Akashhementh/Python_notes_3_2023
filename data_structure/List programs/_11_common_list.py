print("----------------------print common Element form list-------------------------------------")
listA = []
listB = []
print("list-A")
n = int(input("enter the length listA :"))
for i in range(0, n):
    print("enter the element in list-A{}".format(i+1))
    ele = input()
    listA.append(ele)
print("list-B")
m = int(input("Enter the length of listB"))
for j in range(0, m):
    print("Enter the Element in list-B{}".format(j+1))
    elm = input()
    listB.append(elm)
listC = []
print("comparison b/w element in list")
for char in range(0, len(listA)):
    if listA[char] in listB:
        listC.append(listA[char])
print("common ele in both list:", listC)

print("---------------------------------------------------------------------------------------------------------")
listA = [12, 13, 45, "apple"]
listB = [12, 31, 45, "alph"]
listC = []
for i in range(0, len(listA)):
    if listA[i] in listB:
        listC.append(listA[i])
print("common Element in both list:", listC)


