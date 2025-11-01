def remove_smaller_than(numbers: list, limit: int):
    return [num for num in numbers if num >= limit]   # use list comprehension to keep only numbers >= limit

numbers = [1, 65, 32, -6, 9, 11]                     # create a list of numbers
print()
print(remove_smaller_than(numbers, 10))               # print numbers from list that are 10 or greater
print(remove_smaller_than([-4, 7, 8, -100], 0))       # print numbers that are 0 or greater from new list
