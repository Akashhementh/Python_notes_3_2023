print("-------------------------------- find the repeated items of a tuple----------------------------------------")
my_tuple = (10, 20, 30, 40, 50, 50, 60, 70)
my_list = list(my_tuple)
my_repeated_list = []
my_list_1 = []
for i in my_list:
    if i in my_list_1:
        my_repeated_list.append(i)
    else:
        my_list_1.append(i)
my_tuple1 = tuple(my_repeated_list)
print("repeated element", my_tuple1)