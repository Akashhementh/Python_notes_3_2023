print("-----------------------------------------convert list in string---------------------------------------------")
listA = [100, 23, 48, "apple", [10, 50], 45, 67]
string = ""
for i in range(0, len(listA)):
    ele = str(listA[i])
    string += ele + ","
print(string)


print("----------------------------------------------------------------------------------------------------------")
listA = []
n = int(input("Enter the length of the list:"))
string = " "
for i in range(0, n):
    print("Enter the element{}".format(i+1))
    ele = input()
    listA.append(ele)
for i in range(0, len(listA)):
    elm = str(listA[i])
    string += elm + ","
print("the list entered is converted to string", listA, "To string", string)
