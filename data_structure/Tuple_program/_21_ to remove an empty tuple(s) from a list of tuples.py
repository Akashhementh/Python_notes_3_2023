print("----------------- to remove an empty tuple(s) from a list of tuples------------------")
my_list = [(), (1, 2, 4), (3, 4), (23, 45)]
new_my_list = []
for i in my_list:
    if i == ():
        pass
    else:
        new_my_list.append(i)
print(new_my_list)