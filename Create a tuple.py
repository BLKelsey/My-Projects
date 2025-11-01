# Please write a function named create_tuple(x: int, y: int, z: int), which takes three integers as its arguments
# and creates and returns a tuple based on the following criteria:
      # The first element in the tuple is the smallest of the arguments
      # The second element in the tuple is the greatest of the arguments
      # The third element in the tuple is the sum of the arguments

def create_tuple(x: int, y: int, z: int):

          smallest = min(x, y, z)               # Find the smallest of the three
          largest = max(x, y, z)                # Find the largest of the three

          total = x + y + z                     # Find the sum of the three
          return (smallest, largest, total)     # Return a tuple in the requested order


if __name__ == "__main__":
    print()
    print(create_tuple(5, 3, -1))


