# Please write a function named double_items(numbers: list), which takes a list of integers as its argument.
#
# The function should return a new list, which contains all values from the original list doubled. The function should not change the original list.

def double_items(numbers: list):
    list_doubled = []                           # Create an empty list to store the doubled values
    for number in numbers:                      # Loop through each number in the list
        list_doubled.append(number * 2)         # Multiply the individual number by 2
    return list_doubled                         # Return the new list

if __name__ == "__main__":
    print()
    numbers = [2, 4, 5, 3, 11, -4]              # Define my list of numbers
    print('Original list:', numbers)            # Print the original list
    list_doubled = double_items(numbers)        # Call the function
    print('Doubled list:', list_doubled)


