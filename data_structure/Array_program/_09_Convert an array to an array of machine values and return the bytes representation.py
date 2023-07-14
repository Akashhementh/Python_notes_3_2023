print("-----------Convert an array to an array of machine values and return the bytes representation--------------")

import array
arr = array.array('i', [1, 2, 3, 4, 5])
bytes_representation = arr.tobytes()
print("Bytes representation of the array:", bytes_representation)

'''
Bytes representation: The tobytes() method converts the array to an array of machine values and returns 
the bytes representation: bytes_representation = arr.tobytes()
'''