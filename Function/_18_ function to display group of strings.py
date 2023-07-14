print("--------------- function to display group of strings------------")
string = input("Enter the string")

def display(string):
    string1 = string.split()
    for i in string1:
        print(i)

display(string)
