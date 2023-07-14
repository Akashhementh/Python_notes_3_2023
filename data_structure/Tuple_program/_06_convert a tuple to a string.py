print("----------------------convert a tuple to a string-----------------------------------")
my_tuple = (10, 20, 30, 'apple')
new = ''
for i in my_tuple:
    new += ", ".join(i)
print((new))

print("--------------------------------------convert a tuple to a string-------------------------------")
my_tuple = ('apple', 'banana', 'orange')
#tuple_string = ', '.join(['{}'.format(item) for item in my_tuple])
tuple_string = ', '.join([str(item) for item in my_tuple])
print(tuple_string)