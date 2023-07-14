print("--------------Check multiple keys exists in a dictionary----------------------------------")
my_dict = {'akash': 123, 'aman': 345, 'suma': 456, 'ai': 46, 'good': 'sr', 'aka': 123}
listA = ['akash', 'good', 'suma', 'ai']
for i in my_dict.keys():
    if i in listA:
        print(f"{i} exist in the dictionary")
    else:
        print(f"{i} does not exist in the dictionary")

