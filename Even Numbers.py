# Please write a function named even_numbers, which takes a list of integers as an argument.
# The function returns a new list containing the even numbers from the original list.

def even_numbers(my_list):
    evens = []                    # create a new list to store only even numbers
    for num in my_list:
        if num % 2 == 0:
            evens.append(num)    # add it to the new list
    return evens                 # return the new list
print()
my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print('original:', my_list)
print('new:', new_list)




