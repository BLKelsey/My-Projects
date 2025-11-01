#Please write a function named count_matching_elements(my_matrix: list, element: int),
# which takes a two-dimensional array of integers and a single integer value as its arguments.
# The function then counts how many elements within the matrix match the argument value.


def count_and_find_matches(my_matrix: list, element: int):
    count = 0  # counter for matches
    matches = []  # store the actual matches

    for row in my_matrix:                     # loop over each row (list) in the matrix
        for value in row:                     # iterate over each number in the current row
            if value == element:              # check if the number equals the target
                count += 1                    # increase counter IF a match is found
                matches.append(value)         # save the value into matches list

    return count, matches  # return both

if __name__ == "__main__":
    my_matrix = [[1, 2, 1],  [0, 3, 4], [1, 0, 0]]
    count, matches = count_and_find_matches(my_matrix, 1)       # Call the function to count how many 1's are in the matrix
                                                                        # Store the returned values into variables 'count' and 'matches
    print()
    print("There are", count, "matching elements in the matrix and they are:", matches)