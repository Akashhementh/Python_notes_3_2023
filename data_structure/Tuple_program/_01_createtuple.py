print("-----------Create the tuple -------------------")
my_tuple = (1, 2, 'apple', 'orange')
print(my_tuple)

input_string = input("Enter elements of the tuple separated by spaces: ")
input_list = input_string.split()
my_tuple = tuple(input_list)
print(my_tuple)

# ipu = input("Enter the tuple element with space")
# ipu1 = ipu.split()
# print(tuple(ipu1))
