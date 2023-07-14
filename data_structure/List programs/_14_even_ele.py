print("--------------------Remove even elements and print list--------------------------------------------------")
listA = [12, 34, 56, 78, 'apple', 'grape', 'dog', 'cat', (2, 3, 4, 5), [12, 45, 34]]
listB = []
for i in range(0, len(listA)):
    if i % 2 == 0:
        listB.append(listA[i])
print(listB)

print("------------------------------------------------------------------------------------------------")
listA = []
listB = []
n = int(input("enter the length of the list"))
for i in range(0, n):
    print("enter the element{}".format(i+1))
    ele = input()
    listA.append(ele)
print("list u entered",listA)
for i in range(0, len(listA)):
    if i % 2 == 0:
        listB.append(listA[i])
print("Even is:", listB)
