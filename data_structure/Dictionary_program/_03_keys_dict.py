print("------------------Add a key to a dictionary---------------------------")
my_dict = {'akash':123, 'aman': 345, 'suma': 456, 'akki': 456}
n = int(input("Enter the length "))
for i in range(0, n):
    print("Enter the dict {}".format(i+1))
    key = input("Enter the Key")
    value = input("Enter the value")
    my_dict[key] = value
print(my_dict)
print("-----------------------------------------------------------------------")
my_dict = {'akash':123, 'aman': 345, 'suma': 456, 'akki': 456}
my_dict['arun'] = None
print(my_dict)