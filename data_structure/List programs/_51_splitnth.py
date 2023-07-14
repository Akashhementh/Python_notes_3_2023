print("=-split a list every Nth element----------")
listA = [1, 2, 3, 4, 5, 6, 7, 8, 89]
listB = []
n = int(input("enter the range"))
for i in range(0 ,len(listA), n):
    group = listA[i: i+n]
    listB.append(group)
print(listB)

