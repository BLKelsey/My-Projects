# Please write a function named invert(dictionary: dict), which takes a dictionary as its argument.
# The dictionary should be inverted in place so that values become keys and keys become values.

def invert(dictionary):
    inverted = {}                             # Create an empty dictionary where we'll store the swapped key-value pairs
    for key, value in dictionary.items():     # Loop through each key-value pair in the original dictionary
        inverted [value] = key                # Insert into the new dictionary:
                                              # the OLD value becomes the NEW key, and the OLD key becomes the NEW value
    return inverted                           # Return the newly built inverted dictionary


if __name__ == '__main__':
    print()
    dictionary =  {1: "first", 2: "second", 3: "third", 4: "fourth"}
    print('ORIGINAL dictionary key/value: ', dictionary)
    print('INVERTED dictionary value/key: ', invert(dictionary))
