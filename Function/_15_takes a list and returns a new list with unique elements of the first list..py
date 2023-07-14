print("--takes a list and returns a new list with unique elements of the first list.--")
listA = [1, 2, 3, 4, 5, 6, 7, 6, 4, 2, 3]
def unquie(listA):
    listB = []
    listC = []
    for i in listA:
        if i not in listB:
            listB.append(i)
        else:
            listC.append(i)
    return listC
unique_ele = unquie(listA)
print("unique elements of the first list", unique_ele)

