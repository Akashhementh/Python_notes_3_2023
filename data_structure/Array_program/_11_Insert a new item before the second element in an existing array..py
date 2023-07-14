print("-------------Insert a new item before the second element in an existing array.------------")
import array
arr = array.array('i', [1, 2, 3, 4, 5])
new_item = 9
arr.insert(5, new_item)

print("Array after inserting a new item:", arr)
