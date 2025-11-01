# Please write a function named triangle, which draws a triangle of hashes, and takes one argument.
# The triangle should be as tall and as wide as the value of the argument.

def triangle(size):
    for i in range(1, size + 1):
        print("#" * i)

if __name__ == "__main__":
    triangle(6)
    print()
    triangle(3)