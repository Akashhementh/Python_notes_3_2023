print("------------Append items from inerrable to the end of the array-------------")
import array
arr = array.array('i', (1, 2, 3, 4, 5, 6, 7, 8))
ele = (3, 4, 56, 78)
arr.extend(ele)
print(arr)

print("------------------------------------------------------------------------------------")
import array
arr = array.array('i', (1, 2, 3, 4, 5, 6, 7, 8))
ele = (3, 4, 56, 78)
for i in ele:
    arr.append(i)
print(arr)

