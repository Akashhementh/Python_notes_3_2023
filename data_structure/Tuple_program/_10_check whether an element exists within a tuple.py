print("---------------------------check whether an element exists within a tuple------------------------------------")
my_tuple = (10, 20, 30, 40, 50, 50, 60, 70)
n = (input("Enter the Element to find"))
count = 0
for i in my_tuple:
    if n == str(i):
        count += 1
        break
if count == 1:
    print("element exist in the tuple")
else:
    print("Element does not present in the tuple")