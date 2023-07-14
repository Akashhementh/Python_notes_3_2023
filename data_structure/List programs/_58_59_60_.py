print("----------------------Replace the last element in a list with another list----------------------------")
listA = [1, 2, 3, 4, 5]
listB = [2, 3, 4, 5, 6]
for i in listA:
    if i == (len(listA) - 1):
        del listA[i]
        listA.extend(listB)
print(listA)
print("------------------------Check if the n-th element exists in a given list--------------------")
listA = ['apple', 12, 3.4, 'good']
m = input("Enter the nth element")
if listA[-1] == m:
    print("the element is present in the end")
else:
    print("the element is not present")
print("----------------------Find a tuple, the smallest second index value from a list of tuples---------")
listA = [(12, 34), [123,45], 56, (1, 2),(1,1), 'apple']
num = None
for i in listA:
    if isinstance(i, tuple):
        if num is None or i[1] < num:
            num = i[1]
print(num)






