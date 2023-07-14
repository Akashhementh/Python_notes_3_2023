print("-------------------Generate group of five consecutive numbers in a list----------------------")

listA = []
starting = int(input("Enter the starting number"))
ending = int(input("Enter the ending number"))
for i in range(starting, ending+1, 5):
    listB = list(range(i, i+5))
    listA.append(listB)
print(listA)