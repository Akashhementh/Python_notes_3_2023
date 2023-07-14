print("------------------------Create a set-------------------------------------------------------")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("--------------------------------------Iteration over sets-------------------------------")
print("Iteration over set1:")
for item in set1:
    print(item)

print("----------------------------------- Add member(s) in a set-----------------------------------")
set1.add(5)
set1.update([6, 7])

print("-----------------------------------------Remove item(s) from set-------------------------------")
set1.remove(4)
set1.discard(7)

print("------------------------Remove an item from a set if it is present----------------------")
item_to_remove = 3
if item_to_remove in set1:
    set1.remove(item_to_remove)

print("------------------------------- Create intersection of sets------------------")
intersection = set1.intersection(set2)

print("----------------------------------------Create union of sets------------------------------")
union = set1.union(set2)

print("-------------------------------------Create set difference-------------------------------")
difference = set1.difference(set2)

print("---------------------------------Create symmetric difference-----------------------------")
symmetric_difference = set1.symmetric_difference(set2)

print("------------------------------------------Check if set1 is a subset of set2---------------")
is_subset = set1.issubset(set2)

print("-------------------------------Check if set2 is a superset of set1 --------------------------")
is_superset = set2.issuperset(set1)

print("Set 1:", set1)
print("Set 2:", set2)
print("Intersection:", intersection)
print("Union:", union)
print("Difference:", difference)
print("Symmetric Difference:", symmetric_difference)
print("Is Subset:", is_subset)
print("Is Superset:", is_superset)




set1 = {1, 2, 3, 4}

print("-----------------------------------------------Create a shallow copy of a set---------------------------")
set2 = set1.copy()

print("--------------------------------------------------------Clear a set------------------------------------")
set1.clear()

print("------------------------------------------------------Use of frozensets------------------------------------")
frozen_set = frozenset(set2)

print("------------------------------------- Find maximum and minimum value in a set-----------------------------")
maximum_value = max(set2)
minimum_value = min(set2)

print("--------------------------------------------------Find the length of a set------------------------------------")
set_length = len(set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Frozen Set:", frozen_set)
print("Maximum Value:", maximum_value)
print("Minimum Value:", minimum_value)
print("Set Length:", set_length)
