print("---------------------------------Split a list into different variables-----------------------------------")
#listA = ["apple", "bananna", "grape", '23', '23.45', '(12,45)','[23, 5]', "good"]
listA = []
n = int(input("Enter the length"))
for i in range(0, n):
    print("Enter the element{}".format(i+1))
    ele = input()
    listA.append(ele)
for i in range(0, len(listA)):
    print(f"variable{i}", listA[i])
