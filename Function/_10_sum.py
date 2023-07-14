print("---------------------------sum all the numbers in a list-----------------------------------")
def sum_of(listA):
    sum = 0
    for i in listA:
        sum += i
    return sum

listA = [10, 20, 30, 40, 55]
sum_of_number = sum_of(listA)
print("sum of number", sum_of_number)
