print("--Remove the first occurrence of a specified element from an array.--")
import array

arr = array.array('i', [1, 2, 3, 2, 4, 2, 5])
element = 2
for i in arr:                       # Remove all the element
    if i == element:
        arr.remove(element)

print("Array after removing the occurrence of 2 :", arr)

print("--------------------------------------------------------------------------")
import array
arr = array.array('i', [1, 2, 3, 2, 4, 2, 5])
element = 2
arr.remove(element)         # Remove the first occurrence of a specified element from an array

print("Array after removing the first occurrence of 2 :", arr)