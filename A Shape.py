# Please write a function named shape, which takes four arguments:
    # The first two parameters specify a triangle, as above, and the character used to draw it.
    # The first parameter also specifies the width of a rectangle, while the third parameter specifies its height.
    # The fourth parameter specifies the filler character of the rectangle.
# The function prints first the triangle, and then the rectangle below it.


def shape(size, triangle_char, height, rect_filler):
    # Triangle
    for i in range(1, size + 1):
        print(triangle_char * i)

    # Rectangle
    for _ in range(height):
        print(rect_filler * size)


# Example usage
if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")

