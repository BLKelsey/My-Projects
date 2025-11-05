def add_numbers_to_list(numbers: list):
    if len(numbers) % 5 == 0:          # base case: stop when list length is divisible by 5
        return                         # exit the function, ending recursion

    last_number = numbers[-1]          # get the last number in the list
    next_number = last_number + 1      # calculate the next number to add
    numbers.append(next_number)        # add (append) the new number to the end of the list

    add_numbers_to_list(numbers)       # recursive call: run the function again with the updated list


numbers = [1, 3, 4, 5, 10, 11]         # starting list
add_numbers_to_list(numbers)           # call the function to add numbers until length is multiple of 5
print()
print(numbers)
