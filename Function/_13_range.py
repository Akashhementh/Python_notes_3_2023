print("-------------------------check whether a number is in a given range--------------------------------")
number = int(input("Enter the number"))
start = int(input("Enter the starting range"))
end = int(input("Enter the ending range"))

def num(n , s, e):
    if s < n < e:
        return n
    
result = num(number, start,end)
if result:
    print("{} is  the range".format(number))
else:
    print("{} is not range".format(number))


