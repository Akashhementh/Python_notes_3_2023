print("-----------------------------shuffle list(random.shuffle)-------------------------------------------------------")
import random
listA = []
n = int(input("Enter the Length of the list"))
for i in range(0, n):
    print("Enter the element{}".format(i+1))
    ele = input()
    listA.append(ele)
random.shuffle(listA)
print(listA)

print("------------------------------------------(randaom.randint())------------------------------------------------------")
listA = [12, 56, 'apple', 'dog', (2, 3, 4, 5)]
for i in range(len(listA)-1, 0, -1):
    j = random.randint(0, i)
    listA[i], listA[j] = listA[j], listA[i]
print("shuffled list", listA)
print("-----------------------------------just sorting-------------------------------------------------------")
listA = [12, 56, 'apple', 'dog', (2, 3, 4, 5)]
for i in range(len(listA)-1, 0, -1):
    for j in range(len(listA)):
        listA[i], listA[j] = listA[j], listA[i]
print("shuffled list", listA)


