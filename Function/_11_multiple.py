print("------------------------------multiply all the numbers in a list---------------------------------------")
def multiple_of_num(lstA):
    multi = 1
    for i in lstA:
        multi *= i
    return multi

lstA= [10, 30, 45]

multiple_of_num_is = multiple_of_num(lstA)
print("multiple of a number is",multiple_of_num_is)
