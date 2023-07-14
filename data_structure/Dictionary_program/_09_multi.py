print("---------------------multiply all the items in a dictionary----------------------------------------")
my_dict = {'akash': 123, 'aman': 345, 'suma': 456, 'akki': 46, 'good': 'sr'}
value = 1
for j in my_dict.values():
    if isinstance(j, int):
        value = value * j
print(value)
print("---------------------------------------------------------------------------------------------")
# my_dict = {}
# n = int(input("Enter the number of Length"))
# for i in range(0, n):
#     print("Enter the dictionary {}".format(i+1))
#     key = input("Enter Key")
#     value = input("Enter value")
#     my_dict[key] = value
#
# print(my_dict)
# multi = 1
# for char in my_dict.values():
#     if isinstance(char, int):
#         multi *= (int(char))
# print(multi)