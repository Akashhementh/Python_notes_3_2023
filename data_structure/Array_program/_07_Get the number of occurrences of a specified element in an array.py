# print("-------------Get the number of occurrences of a specified element in an array-----------------")
# import array
#
# arr = array.array('i', [1, 2, 2, 3, 2, 4, 2, 5])
# element = 2
#
# occurrences = arr.count(element)
# print("Number of occurrences of", element, "in the array:", occurrences)

print("--------------------------------------------------------------------------------")
import array
arr = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 2, 32, 2, 2, 2])
ele = 2
count = 0
for i in arr:
    if ele == i:
        count += 1
print("Number of occurrences of", ele, "in the array:", count)




