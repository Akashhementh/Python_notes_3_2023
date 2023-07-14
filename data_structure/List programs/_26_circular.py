print("-------------------------------Check circularly identical in two lists---------------------------")
listA = [10, 30, 45, 55]
listB = [30, 45, 10, 55]
if len(listA) == len(listB):
    listC = listA + listA
    for i in listC:
        if i in listB:
            print("Element are circularly")
            break
        else:
            print("element are not circular")
            break
else:
    print("both list are not Equal")

print("--------------------------------------not equal-------------------------------------------------")
listA = [10, 30, 45, 55]
listB = [30, 45, 11, 55]
if len(listA) == len(listB):
    listC = listA + listA
    for i in listC:
        if i in listB:
            print("Element are circularly")
            break
        else:
            print("element are not circular")
            break
else:
    print("both list are not Equal")
