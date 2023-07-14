print("----------------Change the position of every nth value with (n+1)th value---------------------")
listA = [12, 34, "apple", [12, 34, {34, 56}]]
temp = listA[-1]
listA[-1] = listA[0]
listA[0] = temp
print(listA)
print("-----------------------------------------------------------------------------------------")
listA = []
n = int(input("Enter the length of the list-A"))
for i in range(0, n):
    print("enter the element{}".format(i+1))
    ele = input()
    listA.append(ele)
print(listA)
temp = listA[-1]
listA[-1] = listA[0]
listA[0] = temp
print(listA)
