print("-----------------Combine two dictionary adding values for common keys--------------------")
my_dict = {'akash': 123, 'aman': 345, 'suma': 456, 'ai': 46, 'good': 'sr', 'aka': 123}
m_dict = {'akas': 123, 'amn': 345, 'suma': 456, 'a': 46, 'good': 'sr', 'aa': 123}
for i,j in my_dict.items():
    if i in m_dict:
        m_dict[i] += j
    else:
        m_dict[i] = j
print(m_dict)




