print("------------------------table of the given number-------------------------")
number = int(input("Enter the number"))
def table(n):
    for i in range(1, 10+1):
        tab = n*i
        print(n, "*", i, "=", tab)

table(number)

