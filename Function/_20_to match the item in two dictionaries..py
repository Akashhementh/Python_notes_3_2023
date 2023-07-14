print("---------------------------------------to match the item in two dic--------------------------")

def match_items(dict1, dict2):
    matched_items = {}
    for key1, value1 in dict1.items():
        if key1 in dict2 and value1 == dict2[key1]:
            matched_items[key1] = value1
    return matched_items

# Example usage
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 2, "c": 3, "d": 4}
matched = match_items(dict1, dict2)
print("Matched items:", matched)
