'''List'''
'''
SDLC:
           I. REQUIREMENT GATHERING
           II. ANALYSIS
                    1. FUNDAMENTAL ANALYSIS
                    2. TECHNICAL ANALYSIS
            III. DESIGN 
            IV . DEVELOPMENT
            V. DEPLOYMENT/PRODUCTION
REQUIREMENT GATHERING:list of numbers
                            ------------------------------------
                            |    Enter List: |_________|        |
                            |            Submit                 |
                            |___________________________________|
II. ANALYSIS:
            1.FUNDAMENTAL ANALYSIS
            notes: multiply the number in the the list
            scenarios:
                    Empty list Ex: [] : Invalid input
                    special char  ===> no
                    only number  ==> yes 
            2.TECHNICAL Analysis:
            
            state : Data type/int
            Behaviour: operation : +=, ==, * 
                        DM  :   if 
                        loops: yes for
'''
'''
number = [10, 22, 30, 44]
multi = 1
for i in number:
    if number == []:
        print("Invalid Entry")
    else:
         multi = multi * i
print(multi)

listA = []
n = int(input("enter the length"))
multi = 1
for i in range(n):
    print("Enter the number to be multiple {}".format(i+1))
    a = int(input())
    listA.append(a)
for i in listA:
    multi = multi * i
print("multiple", multi)
'''

number = [10, 22, 30, 44, "hello"]
number1 = []
for i in number:
    if str(i).isdigit():
        number1.append(i)
print(number1)
for i in range(0, len(number1)):
    for j in range(0, len(number1)):
        if number1[i] > number1[j]:
            number1[i], number1[j] = number1[j], number1[i]
print(number1[0])





