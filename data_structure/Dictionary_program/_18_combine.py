print("--------------------------Combine values in python list of dictionaries.--------------------------------")
list_of_dicts = [{'name': 'John', 'age': 25, 'city': 'New York'},
                 {'name': 'Alice', 'age': 30, 'city': 'London'},
                 {'name': 'Mike', 'age': 35, 'city': 'Paris'}]
listB = []
for i in list_of_dicts:
    for values in i.values():
        if isinstance(values, str):
            listB.append(values)
        if isinstance(values, int):
            listB.append(values)
print(listB)
print("------------------------------------------------------------------------------------")
item_list = [{'item': 'item1', 'amount': 400},
             {'item': 'item2', 'amount': 300},
             {'item': 'item1', 'amount': 750}]
dic1 = {}
for i in item_list:
    name = i['item']
    amount = i['amount']
    if name in dic1:
        dic1[name] += amount
    else:
        dic1[name] = amount
print(dic1)