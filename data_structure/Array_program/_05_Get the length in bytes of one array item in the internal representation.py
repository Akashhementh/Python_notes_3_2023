print("Get the length in bytes of one array item in the internal representation.")
import array
arr = array.array('i', [1, 2, 3, 4, 5, 6, 7,4,5,6,7,8,9])
iteam_size =arr.itemsize
print("the array size in byte", iteam_size)