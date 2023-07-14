'''List'''
'''
SDLC Phases:
---------------------
        I. REQUIREMENT GATHERING
        II. ANALYSIS
                1. FUNCTIONAL ANALYSIS
                2. TECHNICAL ANALYSIS
        III. DESIGN
        IV. DEVELOPMENT
        V.  TESTING
        VI. DEPLOYMENT/PRODUCTION
        
        
I. REQUIREMENT GATHERING : list of numbers
                            ------------------------------------
                            |    Enter List: |_________|        |
                            |            Submit                 |
                            |___________________________________|
II. ANALYSIS:
================
        1. FUNDAMENTAL Analysis:
        ===========================
        Notes: customer will give string, here we should add the numbers in the list
        
        scenarios: 
                        Empty list       EX: []    : "Invalid string"
                    i.  single number    Ex: [5]   :  "Enter atleast two numbers"
                   ii.  multiple data type  Ex : [23,28,34,94,37,56.78,'hello"]   : "Enter invalid Enter"
                   iii. special chars ==> no
                   iv.  only number ==> yes
        2. TECHNICAL Analysis:
        Entity name : totalsum
        
                state   : Data type/int  
                Behaviour: operators   : += == >=
                           DM          : if 
                           loops       : yes (For loop)

    
'''
number = [10, 20, 30]
num = 0
for i in range(0, len(number)):
    if number == []:
        print("invalid Entry")
    else:
        num += number[i]
print(num)

listA = []
sum = 0
n = int(input("Enter the number of integer in list"))
for i in range(0, n):
    print("enter the number {}".format(i+1))
    ele = int(input())
    listA.append(ele)
for i in listA:
    sum = sum+i
print(sum)
