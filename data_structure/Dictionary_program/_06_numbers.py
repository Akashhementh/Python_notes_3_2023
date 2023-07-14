print("--Print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys--")
n = int(input("enter the length"))
my_dict = {x: x*x for x in range(1, n+1)}
print(my_dict)

