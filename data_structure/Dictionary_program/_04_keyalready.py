print("-----------------------Check if a given key already exists in a dictionary.------------------------")
my_dict = {'akash': 123, 'aman': 345, 'suma': 456, 'akki': 456}
print("Enter the key to be found")
key = input("Enter the Key")
if key in my_dict:
    print(f"The key {key} is present")
else:
    print(f"The key {key} is not present")
print("---------------------------------------------------------------------")



