print("Generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)")
my_dict = {}
n = int(input("Enter the length"))

my_dict = {x: x*x for x in range(1, n)}
for keys, values in my_dict.items():
    print(f"({keys}:{values})")

# n = int(input("Enter a number: "))
#
# # Generate the dictionary using a dictionary comprehension
# my_dict = {x: x*x for x in range(1, n+1)}
#
# # Print the dictionary
# for key, value in my_dict.items():
#     print(f'({key}, {value})')
