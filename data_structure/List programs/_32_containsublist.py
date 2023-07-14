print("---------------------------------------Check a list contains sublist-------------------------------")

listA = []
n = int(input("Enter the length of the list: "))
for i in range(0, n):
    print("Enter element {}: ".format(i + 1))
    ele = input()
    listA.append(ele)

listC = []
for char in listA:
    if char.startswith('[') or char.endswith(']'):
        sub_ist = char[1:-1].split(',')
        sub_list = []
        for e in sub_ist:
            if e.startswith('[') or e.endswith(']'):
                su_st = char[1:-1].split(',')
            sub_list.append(eval(e.strip()))
        listC.append(sub_ist)

    if char.startswith('(') and char.endswith(')'):
        sub_ist = char[1:-1].split(',')
        sub_list = []
        for e in sub_ist:
            sub_list.append(eval(e.strip()))
        listC.append(sub_list)
    elif "." in char:
        listC.append(float(char))
    else:
        listC.append(char)
# listA = [10,23,34,[23,[45,54]],[45,67],[34,(3,6,7),45]
for i in listC:
    if isinstance(i, (list, tuple)):
        print(f"The list contains a list or tuple: {i}")
        for j in i:
            if isinstance(j, (list, tuple)):
                print(f"The list contains a sublist: {j}")
                print("It contains a sublist")
else:
    print("The List does not contain a sublist.")


