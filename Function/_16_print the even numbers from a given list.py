print("print the even numbers from a given list")

listA = [1,2,3,4,5,6,7,8]

def even_number(listA):
    for i in listA:
        if i % 2 == 0:
            print(i)

even_number(listA)
