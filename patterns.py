def square_pattern(size):
    for i in range(size):
        for j in range(size):
            print("*", end=" ")
        print()

# Input the size of the square
square_size = int(input("Enter the size of the square: "))
square_pattern(square_size)


def left_triangle_pattern(height):
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

# Input the height of the left triangle
left_triangle_height = int(input("Enter the height of the left triangle: "))
left_triangle_pattern(left_triangle_height)


def right_triangle_pattern(height):
    for i in range(1, height + 1):
        spaces = height - i
        stars = i
        print(" " * spaces + "*" * stars)

# Input the height of the right triangle
right_triangle_height = int(input("Enter the height of the right triangle: "))
right_triangle_pattern(right_triangle_height)



def rhombus_pattern(height):
    for i in range(1, height + 1):
        spaces = height - i
        stars = i
        print(" " * spaces + "* " * stars)

    for i in range(height - 1, 0, -1):
        spaces = height - i
        stars = i
        print(" " * spaces + "* " * stars)

# Input the height of the rhombus
rhombus_height = int(input("Enter the height of the rhombus: "))
rhombus_pattern(rhombus_height)
