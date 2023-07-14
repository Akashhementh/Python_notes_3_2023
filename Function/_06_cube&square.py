print("------find the cube and square of the number--------------------------")
number = int(input("Enter the number"))

def cube_square(n):
    cube = n**3
    square = n**2
    return cube, square

cube, square = cube_square(number)
print("the cube is : {} and square is  : {} of the number: {}".format(cube, square, number))