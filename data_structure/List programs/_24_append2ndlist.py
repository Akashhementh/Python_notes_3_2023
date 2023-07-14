print("-------------------append a element from the list1 to list2------------------------------------------------")
listA = ["lion", 34, "apple",[23, 54, 89]]
listB = [10, "Tiger"]
for i in listA:
    listB.append(i)
print(listB)

print("-------------------------or------------------------------------------------------------")
listA = ["lion", 34, "apple",[23, 54, 89]]
listB = [10]
listC = listA + listB
print(listC)
