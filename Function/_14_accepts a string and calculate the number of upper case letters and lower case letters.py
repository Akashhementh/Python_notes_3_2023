print("-accepts a string and calculate the number of upper case letters and lower case letters--")
string = (input("Enter the string"))
def upper_lower(s):
    count_upper = 0
    count_lower = 0
    for i in s:
        if i.isupper():
            count_upper += 1
        elif i.islower():
            count_lower += 1
    return count_upper, count_lower
count_upper_case , count_lower_case = upper_lower(string)
print(" number of upper case letter is {} and lower case letter {}".format(count_upper_case, count_lower_case))


