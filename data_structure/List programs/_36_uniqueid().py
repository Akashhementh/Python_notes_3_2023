print("-------------------------Variable unique identification number-------------------------------")
listA = []
n = int(input("Enter the length of the list"))
for i in range(0, n):
    print("enter the element{}".format(i+1))
    ele = input()
    listA.append(ele)
print(listA)

listID = {}
listType = {}
for i in listA:
    listID[i] = id(i)
    listType[i] = type(i)
print("the id of Each variable", listID)
print("The type of Each Variable", listType)
print("---------------------------------------------------------------------------------------------------")
listA = [23, 45, [34, 45, (34, 56)], "apple", 45]
listID = {}
listType = {}
for i in listA:
    j = str(i)
    listID[j] = id(j)
    listType[j] = type(j)
print("the id of Each variable", listID)
print("The type of Each Variable", listType)
