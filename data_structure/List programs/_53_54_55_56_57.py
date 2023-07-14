'''---------53 === 54=== 55 === 56 === 57=== -----------------------------'''
print("-------------------------------------Create a list with infinite elements-----------------------")
infinity = []
n = int(input("Enter the infinite number till you want to print"))
for i in range(n+1):
    infinity.append(i)
print(infinity)
print("--------------------Concatenate elements of a list---------------------------------------------")
listA = ['this', 'is', 'akash']
print(' '.join(listA))
print("")
print("----------------Remove key values pairs from a list of dictionaries----------------------------")
listA = [{'akash': 234}, {'guru': 345}, {'eru': 678}, {'guru': 456}, {'yuno': 567}]
for i in listA:
    i.pop('guru', None)
print(listA)
print("------------------------------------Convert a string to a list-------------------------------------")
listA = []
string = "this is akash 123 45"
string1 = string.split()
for i in string1:
    try:
        ele = int(i)
        listA.append(ele)
    except ValueError:
        listA.append(i)
print(listA)

print("--------------------------Check if all items of a list is equal to a given string-----------------")
listA = ["akash", "akash", "akash"]
string = "akash"
count = 0
for i in listA:
    if i == string:
        count += 1
    else:
        print("the element in the list not equal")
    if count == len(listA):
        print("All the elements all equal")

