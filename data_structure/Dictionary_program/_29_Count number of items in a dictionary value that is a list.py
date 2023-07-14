print("-------------------------Count number of items in a dictionary value that is a list-----------------------------------")
dictA = {'key1':[1,1,2,3,4,5,6], 'keys': (1,2,3,4), 'keys1':"akash"}
count = 0
for keys, values in dictA.items():
    if isinstance(values, list):
        for i in values:
            count += 1
print("the number of values in a list:", count)

