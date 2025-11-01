# Please write a function named count_matching_elements(my_matrix: list, element: int),
# which takes a two-dimensional array of integers and a single integer value as its arguments.
# The function then counts how many elements within the matrix match the argument value.

def count_matching_elements(my_matrix: list, element: int):
    count = 0                      # Initialize counter
    for row in my_matrix:          # Loop through each row
       for value in row:           # Loop through each value in the row
           if value == element:
               count += 1          # increase count if match found
    return count

if __name__ == "__main__":
    print()
    my_matrix =  [[1, 2, 1], [0, 3, 4], [1, 0, 0]]

    # Calls the function "count_matching_elements" with two arguments:
    # my_matrix → the two-dimensional list (matrix) of integers
    # 1 → the integer value we want to count inside the matrix
    # The function will return the total number of times the value 1 appears in my_matrix.
    print("There are", count_matching_elements(my_matrix, 1), "matching elements in the matrix")






