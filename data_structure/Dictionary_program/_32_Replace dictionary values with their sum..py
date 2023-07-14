print("-----------------Replace dictionary values with their sum-----------------------------")
dictA = {'key1': [1, 2, 3], 'key2': [4, 5, 6], 'key3': [7, 8, 9]}
for key in dictA:
    dictA[key] = sum(dictA[key])
print("Updated Dictionary:", dictA)




