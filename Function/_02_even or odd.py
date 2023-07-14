# print("--------------------------------------------------print even and odd numbers------------------------------------")
#
# num = int(input("Enter the number "))
# def is_number(n):
#     if n % 2 == 0:
#         print("its an even number")
#     else:
#         print("its an odd number")
#
# is_number(num)
#
# print("----------------------------------------------------------------------------------------------------")
# def number(n):
#     if n % 2 == 0:
#         return True
#
# num = int(input("Enter the number"))
#
# result = number(num)
#
# if result:
#     print("its an even number")
# else:
#     print("its an odd number")
#
#
#

print("----------------------------------------------------------------------------------------------")
str1 = 'aaabbaaccddbccc'
count = 1
char_count = []
current_char = str1[0]
for i in str1[1:]:
    if i == current_char:
        count += 1
    else:
        char_count.append((current_char,count))
        current_char = i
        count = 1
char_count.append((current_char, count))
for char, count in char_count:
    print(f"{char}:{count}", end=',')





















