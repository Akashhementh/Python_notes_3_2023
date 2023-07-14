print(" ----------------------------------replace last value of tuples in a list-----------------------------------------------------")
my_list =[(1, 2), (3, 4), (4, 5), (6, 7)]
new_my_list = []
for item in my_list:
    new_list = item[:-1] + (10,)
    new_my_list.append(new_list)
print("updated List:", new_my_list)