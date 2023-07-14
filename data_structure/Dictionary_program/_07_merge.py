print("----------------------------------Merge two Python dictionaries----------------------------------------")
my_dict = {'akash': 123, 'aman': 345, 'suma': 456, 'akki': 456}
m_dict = {'a': 1, 'b': 2}
r_dict = {**my_dict, **m_dict}
print(r_dict)
print("-----------------------------------------------------------------------------------------------------------")
my_dict = {'akash': 123, 'aman': 345, 'suma': 456, 'akki': 456}
m_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.update(m_dict)
print(my_dict)
