print("-------------------------------find the Max of three numbers----------------------------------------")
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the third number"))

def maximum_number(a, b, c):
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    return maximum
result = maximum_number(a, b, c)

print("maximum of three number is :", result)


