def rows_of_stars(numbers: list): return ["*" * num for num in numbers]  # Create a list of star strings, each '*' repeated 'num' times

numbers = rows_of_stars([1,2,3,4])  # Generate rows of stars for the list [1,2,3,4]
print()  # Print a blank line for spacing

for num in numbers: print(num)  # Print each row of stars
print()  # Another blank line between outputs

numbers = rows_of_stars([4, 3, 2, 1, 10])  # Generate rows of stars for the list [4,3,2,1,10]
for num in numbers:
    print(num)  # Print each row of stars

