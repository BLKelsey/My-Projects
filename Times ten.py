# Please write a function named times_ten(start_index: int, end_index: int), which creates and returns a new dictionary.
# The keys of the dictionary should be the numbers between start_index and end_index inclusive
#
# The value mapped to each key should be the key times ten.

def times_ten(start_index: int, end_index: int):
    my_dict = {}                                               # Create an empty dictionary to store results

    for number in range(start_index, end_index + 1):          # Loop through each number from start_index to end_index
                                                              # range(end_index + 1) is used because range normally stops before the last number.

        my_dict[number] = number * 10                         # Add a new key-value pair:
                                                                  #   key = the current number
                                                                  #   value = that number multiplied by 10

    return my_dict                                            # Return the completed dictionary

dict = times_ten(3, 6)                    # Call the function with start_index = 3 and end_index = 6

print()
print("3 * 10, 4 * 10, 5 * 10, 6 * 10 = ")
print(dict)

