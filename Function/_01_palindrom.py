print("--------------------------check given word is palindrome or not------------------------------------")
word = input("Enter the word")
def is_palindrom ( palindrom_word ):
    reverse_word = word[::-1]
    if reverse_word == word:
        print("its an palindrom", reverse_word)
    else:
        print("its not an palindrom", reverse_word, word)
is_palindrom (word)


print("print even and odd numbers")

num = input("Enter the number ")
def is_number(n):
    if n % 2 == 0:
        print("its an even number")
    else:
        print("its an odd number")
is_number(num)

def number(n):
    if n % 2 == 0:
        return True
    else:
        return False
num = input ("Enter the number")

result = number(num)

if result:
    print("its an even number")
else:
    print("its an odd number")

