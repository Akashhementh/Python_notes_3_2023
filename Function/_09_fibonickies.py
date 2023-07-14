print("-------------------------------fibonacci series?------------------------")
def fibonnicies(n):
    if n == 0:
        return n
    if n == 1:
        return n
    else:
       n = fibonnicies(n-1) + fibonnicies(n-2)
       return n

number = int(input("Enter the number"))

for i in range(0, number+1):
    print(fibonnicies(i))



