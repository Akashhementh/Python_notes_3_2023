print("------------------------------------------------Frequency of Element----------------------------------")
listA = [1, 2, 3, 4, 2, 1, 3, 4, 3, 3, 2, "apple", "apple"]
frq = {}
for i in range(0, len(listA)):
    if listA[i] in frq:
        frq[listA[i]] += 1
    else:
        frq[listA[i]] = 1
print("the number of time element repeated", frq)