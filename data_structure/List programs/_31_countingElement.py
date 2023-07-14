print("-----------------------------Counting number elements with in a specified ranges---------------------")
listA = []     # ['apple', '34', '67', 'bananna', '89.9', '[45,56,7]', '(10,30,45)', '97']
listB = []
n = int(input("Enter the length"))
for i in range(0, n):
    print("Enter the Element {}".format(i+1))
    ele = input()
    listA.append(ele)
print("The entered list:", listA)
start = int(input("enter the starting range="))
end = int(input("enter the end range="))
if (end - 1) > len(listA):
    print("invalid range")
else:
    for i in range(0, len(listA)):
        if (i >= (start-1)) and (i <= (end-1)):
            listB.append(listA[i])
print(f"As per your specification range {start} and {end}", listB, "count is", len(listB))

print("-------------------------------------------------------------------------------------------")
listA = ['apple', 34, 67, 'bananna', 89.9, [45,56,7], (10,30,45), 97]


