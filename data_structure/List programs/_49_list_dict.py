print("---------------------------Convert list to list of dictionaries------------------------------------")
listA = [12, 34, 5.6, 6.7, "apple", "orange"]
number = {'num': []}
float_value = {'float': []}
alph = {'fruit': []}
for i in listA:
    if isinstance(i, int):
            number['num'].append(i)
    elif isinstance(i, float):
        float_value['float'].append(i)
    elif isinstance(i, str):
        alph['fruit'].append(i)
print(number)
print(float_value)
print(alph)





