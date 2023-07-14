print("Convert an array to an ordinary list with the same items.")
import array
arr = array.array('i', [1, 2, 3, 4, 5])
lst = arr.tolist()
print("List representation of the array:", lst)

