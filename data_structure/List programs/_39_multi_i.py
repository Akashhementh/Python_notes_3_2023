print("-------------------Converting multiple integers into single integer---------------------------")
listA = [1, 2, 3, 4, 5]
listB = ""
for i in listA:
    listB += str(i)
print(listB)
print("-------------------------------------------------------------------------------------------------")
listA = []
n = int(input("Enter the length"))
for i in range(0, n):
    print("Enter the element{}".format(i+1))
    ele = input()
    listA.append(ele)
listB = []
listC = []
for i in listA:
    if i.isdigit():
        listB.append(i)
    else:
        listC.append(i)
string = ''
for i in listB:
    string += i+','
print(string)


