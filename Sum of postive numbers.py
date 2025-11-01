# Please write a function named sum_of_positives, which takes a list of integers as its argument.
# The function returns the sum of the positive values in the list.

def sum_of_positives(my_list):
    result = 0
    for num in my_list:       # loop through each number in the list
        if num > 0:           # only add positive numbers
            result += num     # add the current number to the running total
    return result             # after checking all numbers, return the total sum

# main program
my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)   # call the function to calculate the sum of positives
print("The result is", result)



