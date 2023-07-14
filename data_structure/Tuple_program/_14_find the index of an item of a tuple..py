print("---------------------------------find the index of an item of a tuple.---------------------------")
my_tuple = (1, 2, 3, 4, 5, 6, 7)
n = int(input("Enter the element"))
for i in range(0, len(my_tuple)):
    if n == my_tuple[i]:
        print(i)
