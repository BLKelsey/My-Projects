# Please write a function named square_of_hashes, which draws a square of hash characters.
# The function takes one argument, which determines the length of the side of the square.


def box_of_hashes(size):
    for row in range(size):
        print("#" * size)

if __name__ == '__main__':
    box_of_hashes(5)
    print()
    box_of_hashes(2)

