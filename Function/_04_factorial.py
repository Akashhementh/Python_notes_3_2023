print("-------------------------------factorial of given number----------------------")
num = int(input("Enter the factorial number"))
def factorial(number):
    multi = 1
    for i in range(1, number+1):
        multi *= i
    return multi

result = factorial(num)
print(f"factorial of {num} is ", result)
print("--------------------------------------------------------------")





