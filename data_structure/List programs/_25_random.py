print("--------------------------------------Finding a second smallest number-----------------------------")
listA = []
n = int(input("Enter the length of the list"))
for i in range(0, n):
    print("Enter the Element{}".format(i+1))
    ele = input()
    listA.append(ele)
listB = []
for i in listA:
    if str(i).isdigit():
        listB.append(i)
print(listB)