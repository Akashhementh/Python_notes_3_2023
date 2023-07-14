print("-------------------Find missing and additional values-------------------------------------")
listA = [1, 2, 3, 4, 5, 6, 'apple', 8.9, 10]
listB = [4, 5, 6, 7, 8, 9, 'apple', 7.9, 10]
listC = []
listD = []
for i in listA:
    if i not in listB:
        listC.append(i)
for j in listB:
    if j not in listA:
        listD.append(j)
print(f"Element un equal in listB-->{listA}", listC)
print(f"Element un equal in listA-->{listB}", listD)


