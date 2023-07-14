print("-------------------------Split a list based on first character of word--------------")
#listA = ["apple", "bananna", "grape", '23', '23.45', '(12,45)','[23, 5]', "good"]
listA = []
n = int(input("Enter the length"))
for i in range(0, n):
    print("Enter the element{}".format(i+1))
    ele = input()
    listA.append(ele)
listB = []
for i in listA:
    if i.startswith('{') or i.startswith('[') or i.startswith('('):
        continue
    if i.isdigit():
        continue
    if "." in i:
        continue
    else:
        listB.append(i)
good = {}
for i in listB:
    first = i[0]
    if first in good:
        good[first].append(i)
    else:
        good[first] = [i]
print(good)
