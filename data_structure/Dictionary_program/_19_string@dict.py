print("------------------Create a dictionary from a string.------------------------------------------")
listA = ['akash', 45, 87, 'akash']
my_dict = {}
for i in listA:
    if isinstance(i, int):
        if 'num' in my_dict:
            my_dict['num'].append(str(i))
        else:
            my_dict['num'] = [str(i)]
    if isinstance(i, str):
        first_word = i[0]
        if i[0] in my_dict:
            my_dict[first_word].append(i)
        else:
            my_dict[first_word] = [i]
print(my_dict)