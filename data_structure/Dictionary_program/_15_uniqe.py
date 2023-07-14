print("------------Print all non unique values in a dictionary----------------------- ")
my_dict = {'akash': 123, 'aman': 345, 'suma': 456, 'ai': 456, 'good': 'sr', 'aka': 123}
value_repeated =[]
for keys, values in my_dict.items():
    if values not in value_repeated:
        value_repeated.append(values)
    else:
        print(f"repeated values= {keys}: {values}")


print("------------Print all unique values in a dictionary----------------------- ")
my_dict = {'akash': 123, 'aman': 345, 'suma': 456, 'ai': 456, 'good': 'sr', 'aka': 123}
value_repeated =[]
for keys, values in my_dict.items():
    if values not in value_repeated:
        value_repeated.append(values)
        print(f"repeated values= {keys}: {values}")

