print("------------------------------------access index in the list--------------------------------------")
listA = [100, 23, 48, "apple", [10, 50], 45, 67]
index1 = (input("Enter the index number to create separate list with ',': "))
listB = []
index = index1.split(',')
for i in range(0, len(listA)):
    if str(i) in index1:
        listB.append(listA[i])
print("The Requested index list", listB)

