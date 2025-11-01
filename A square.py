#Please write a function named square, which prints out a square of characters, and takes two arguments.
# The first parameter specifies the length of the side of the square.
# The second parameter specifies the character used to draw the square.


def square(length,char):
    for _ in range(length):
        print(length * char)

if __name__ == '__main__':
    square(5, "*")
    print()
    square(3, "o")



