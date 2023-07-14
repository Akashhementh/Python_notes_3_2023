print("----------------------print given Pascal's triangle--------------------------")
def pascal_value(n):
    for i in range(1, n):
        res = 11**i
        print(res)

number = int(input("Enter the number:"))
pascal_value(number)

print("------------------------------------------------------------------------------")
def print_pascals_triangle(rows):
    triangle = []

    for row in range(rows):
        current_row = []
        for column in range(row + 1):
            if column == 0 or column == row:
                current_row.append(1)
            else:
                previous_row = triangle[row - 1]
                current_row.append(previous_row[column - 1] + previous_row[column])
        triangle.append(current_row)

    for row in triangle:
        print(' '.join(str(num) for num in row), end=' ')

# Print Pascal's triangle with 6 rows
print_pascals_triangle(6)
