# Please write a function named range_of_list, which takes a list of integers as an argument.
# The function returns the DIFFERENCE between the smallest and the largest value in the list.

range_of_list = [12, 4, 35, 9, 62]
smallest = min(range_of_list)
largest = max(range_of_list)
result = largest - smallest
print('The range of the list, which is largest value - smallest value is: ',result)