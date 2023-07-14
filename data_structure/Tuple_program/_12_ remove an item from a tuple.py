print("----------------------------------- remove an item from a tuple---------------------------------")
my_li = (10, 20, 30, 40, 50, 50, 60, 70)
my_list = []
ele_to_remove = 30
for i in my_li:
    if i == ele_to_remove:
        pass
    else:
        my_list.append(i)
print(tuple(my_list))