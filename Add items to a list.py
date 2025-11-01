# Please write a program which first asks the user for the number of items to be added.
# Then the program should ask for the given number of values, one by one, and add them to a list in the order they were typed in.
# Finally, the list is printed out.

items = int(input("How many items do you want to add? "))

# Create an empty list
numbers = []

# Loop exactly 'items' times
for _ in range(items):
    value = input("Enter a value: ")
    numbers.append(value)

# Print the list
print(numbers)

