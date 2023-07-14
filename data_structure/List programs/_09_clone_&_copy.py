print("-------------------------------------using slicing method----------------------------------------")
listA = [12, 34, 56, 78]                   # |  clone
listB = listA[:]                           # |
print(listA)

print("------------------------------- copy function method -------------------------------------------------")
import copy
listA = [12, 34, 56, 78]                   # |  copy
listB = copy.copy(listA)
print(listB)
print("---------------------------------- using for Loops------------------------------------------------------")
listA = [12, 34, 56, 78]
listB = []
for i in range(0, len(listA)):
    listB.append(listA[i])
print(listB)
