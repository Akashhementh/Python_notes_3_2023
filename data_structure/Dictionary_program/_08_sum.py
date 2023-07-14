print("---------------------Sum all the items in a dictionary----------------------------------------")
my_dict = {'akash': 123, 'aman': 345, 'suma': 456, 'akki': 46, 'good': 'sr'}
value = 0
for j in my_dict.values():
    if isinstance(j, int):
        value += j
print(value)
print("---------------------------------------------------------------------------------------------")
my_dict = {}
n = int(input("Enter the number of Length"))
for i in range(0, n):
    print("Enter the dictionary {}".format(i+1))
    key = input("Enter Key")
    value = input("Enter value")
    my_dict[key] = value
sum = 0
for j in my_dict.values():
    if isinstance (j, int):
        sum += j
print(sum)

