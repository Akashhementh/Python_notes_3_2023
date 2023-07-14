print("-------------------Create a list by concatenating a given list which range goes from 1 to n----")
#listA = [10, 23, 45, 56,"apple"]
listA = []
n = int(input("Enter the length of the list"))
for i in range(0, n):
    print("enter the element{}".format(i+1))
    ele = input()
    listA.append(ele)
print(listA)
start = int(input("Enter the number range starting"))
ending = int(input("Enter the number range ending"))
listB = listA + list(range(start, ending+1))
print(f"the range is added to the given {listA}concatenated{listB}")
