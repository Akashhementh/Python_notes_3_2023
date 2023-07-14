# print("---------------Prints each item and its corresponding type from the following list.----------------")
# listA = [{'akash': 1234}, 'hementh', 2344, 'ganesh', 57.89, {345, 7890}, (23,54), [23, 45, [67, 89]]]
# for i in listA:
#     print(f"{i} the type of Data", type(i))
print("------------------------------------------------------------------------------------------------")
di = {}
n = int(input("Enter the length"))
for i in range(0, n):
    print("Enter the Element{}".format(i+1))
    key = input("keys")
    values = input("values")
    di[key] = values
print(di)

