print("-----------------------------------Finding index of an item in specified list---------------------------")
listA = [100, 23, 48, "apple", [10, 50], 45, 67]
print("This is the list:", listA)
element = 67
index = -1
for i in listA:
    if isinstance(i, list):
        if element in i:
            index = i.index(element)
            print(f"Index of {element} in {i} tuple: {index}")
            break
    elif i == element:
        index = listA.index(i)
        print(f"index of {element} in list: {index} ")
        break

if index != -1:
    print(f"Index of '{element}' in nested list: {index}")
else:
    print(f"'{element}' not found in nested list")




