# Please write a function named distinct_numbers, which takes a list of integers as its argument.
# The function returns a new list containing the numbers from the original list in order of magnitude, and so that each distinct number is present only once.

def distinct_numbers(my_list):
    new_list = []
    for item in my_list:
        if item not in new_list:    # only add the number if it's not already in the list
            new_list.append(item)



    return sorted(new_list)         # return the list of distinct numbers, sorted in ascending order
                                    # - sorted() arranges the numbers from smallest to largest
                                    # - ensures duplicates are removed because we only appended unique items
my_list = [1, 1, 2, 3, 3, 4, 4, 5, 11, 11, 30]
new_list = distinct_numbers(my_list)
print(new_list)
