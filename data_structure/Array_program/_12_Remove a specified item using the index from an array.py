print("----------------------Remove a specified item using the index from an array.----------------")
import array as arr
number = arr.array('i', [1, 2, 3, 4, 5, 6])
number.remove(2)   #remove the element
print(number)
print("-----------------------------------------")
import array
number = array.array('i', [1, 2, 3, 4, 5, 6])
number.pop(5)     # remove index value
print(number)
