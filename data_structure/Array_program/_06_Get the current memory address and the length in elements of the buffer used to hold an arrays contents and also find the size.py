print("-Get the current memory address and the length contents and also find the size ")
import array
arr = array.array('i', [1, 2, 3, 4, 5, 6, 7, 89])
buffer_address = arr.buffer_info()[0]
buffer_length = arr.buffer_info()[1]
print("Memory address of the buffer:", buffer_address)
print("Length in elements of the buffer:", buffer_length)

'''
Memory address and buffer information: The buffer_info() method provides the current memory address and 
the length in elements of the buffer used to hold 
the array's contents. For example: buffer_address = arr.buffer_info()[0] and buffer_length = arr.buffer_info()[1].
'''