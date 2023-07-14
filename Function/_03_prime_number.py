print("---------------Enter the prime number-----------------------------")
def is_prime(number):
    if number < 2:
        return False
    elif number > 2:
        for i in range(2, int(number**0.5)+1):
            if number % i == 0:
                return False
        return True
start = int(input("Enter the starting number"))
end = int(input("enter the ending number"))

for num in range(start,end+1):
   if is_prime(num):
    print(num)


