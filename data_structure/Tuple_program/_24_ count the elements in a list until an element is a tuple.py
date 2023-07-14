print("-------------------- count the elements in a list until an element is a tuple---------------------")

my_list = [1, 2, 3, "Hello", ("apple", "banana"), 4, 5]
count = 0
for element in my_list:
    if isinstance(element, tuple):
        break
    count += 1
print("Number of elements until a tuple:", count)
