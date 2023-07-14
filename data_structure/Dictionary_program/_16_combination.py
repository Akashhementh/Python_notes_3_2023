print("Create and display all combinations of letters, selecting each letter from a different key in a dictionary")
my_dict = {'akash': 123, 'aman': 345, 'suma': 456, 'ai': 456, 'good': 'sr', 'aka': 123}
combine = []
for keys, values in my_dict.items():
    combine.append(keys)

print(''.join(combine))









