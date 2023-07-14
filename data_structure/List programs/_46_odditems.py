print("----------------------------------------Select odd items of a list---------------------------------------")
listA = []
n = int(input("Enter the length"))
for i in range(0, n):
    print("Enter the element{}".format(i+1))
    ele = input()
    listA.append(ele)
listB = []
for i in range(0, len(listA)):
    if i % 2 == 0:
        continue
    else:
        listB.append(listA[i])
print("The odd Element from the list", listB)
print("---------------------------------------------------------------------")