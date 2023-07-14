# print("---------------------------------------Check a list contains sublist-------------------------------")
# listA = []                              #listA = [23, 45, [56, 78], "apple", 8, [56, 67, (89, 67)], 10]
# n = int(input("Enter the length of the list"))
# for i in (0, n):
#     print("Enter the element{}".format(i+1))
#     ele = input()
#     listA.append(ele)
#     print(listA)
listA = [23, 45, [56, 78], "apple", 8, [56, 67, (89, 67)], 10]
for i in listA:
    if isinstance(i, (list, tuple)):
        print(f"The list contain list or tuple{i}")
        for j in i:
            if isinstance(j, (list, tuple)):
                print(f"The list contain list/tuple inside list/tuple {j}")
else:
    print("the list does not contain substring:")