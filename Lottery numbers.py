# Please write a function named lottery_numbers(amount: int, lower: int, upper: int), which generates as many random numbers as specified by the first argument.
# All numbers should fall within the bounds lower to upper. The numbers should be stored in a list and returned.
# The numbers should be in ascending order in the returned list.
#
# As these are lottery numbers, no number should appear twice in the list.

import random

def lottery_numbers(amount: int, lower: int, upper: int):
    numbers = []

    while len(numbers) < amount:
        new_num = random.randint(lower, upper)

        if new_num not in numbers:
            numbers.append(new_num)
            numbers.sort()

    return numbers

# Generate numbers
result = lottery_numbers(7, 1, 40)

# Print each number on a new line
for num in result:
    print(num)



