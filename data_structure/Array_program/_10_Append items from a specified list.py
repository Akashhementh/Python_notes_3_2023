print("-----------------------------------------Append items from a specified list.-------------------")

import array
arr = array.array('i', [1, 2, 3, 4, 5])
lst = [6, 7, 8]
arr.fromlist(lst)
print("Array after appending items from list:", arr)

print("--------------------------------------------------------------------------------------------")

import array
arr = array.array('i', (1, 2, 3, 4, 5))
lst = (1, 2, 3, 4)
for i in lst:
    arr.append(i)
print("Array after appending items from list:", arr)

print("--------------------------------------------------------------------------------------------")

import array
arr = array.array('i', [1, 2, 3, 4, 5])
lst = [6, 7, 2, 3, 4]
arr.extend(lst)
print("Array after appending items from list:", arr)

print("-----------------------------------------------------------------------------------------------")