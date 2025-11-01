# Please write a function named remove_smallest(numbers: list), which takes a list of integers as its argument. The
# functions should find and remove the smallest item in the list. You may assume there is a single smallest item in the list.
# The function should not have a return value - it should directly modify the list it receives as a parameter.

def remove_smallest(numbers: list):
    if not numbers:
        return numbers
    smallest = min(numbers)         # Find the smallest number
    numbers.remove(smallest)        # Remove the smallest number from the list
    return numbers                  # Return the updated list

if __name__ == '__main__':
    print()
    numbers = [2, 4, 6, 1, 3, 5]
    print(numbers)
    print('The smallest number removed is: ',min(numbers))
    numbers = remove_smallest(numbers)
    print('Updated list:', numbers)





