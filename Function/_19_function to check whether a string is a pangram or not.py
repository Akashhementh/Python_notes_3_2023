print("--function to check whether a string is a pangram or not--")
def is_pangram(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    string = string.lower()
    for char in alphabet:
        if char not in string:
            return False
    return True

input_string = input("Enter a string: ")

if is_pangram(input_string):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")

