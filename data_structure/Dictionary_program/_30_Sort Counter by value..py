print("---------sort Counter by values--------------------------------")
dictA = {'key1': [1, 5, 2, 4, 3], 'key2': [9, 6, 7, 8], 'key3': [10, 12, 11]}

sorted_dict = {key: sorted(value) for key, value in dictA.items()}

print("Sorted Dictionary:")
for key, value in sorted_dict.items():
    print(key, ":", value)
