print("_-------unzip a list of tuples into individual lists._--------------------------")
my_list = [("a", 1), ("b", 2), ("c", 3)]
unzipped = list(zip(*my_list))
print(unzipped)
print("unzipped lists:")
for item in unzipped:
    print(item)
