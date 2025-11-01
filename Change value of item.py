# Please write a program which initializes a list with the values [1, 2, 3, 4, 5].
# Then the program should ask the user for an index and a new value, replace the value at the given index, and print the list again.
# This should be looped over until the user gives -1 for the index. You can assume all given index values will fall within your list.

numbers = [1, 2, 3, 4, 5]

while True:
    index = int(input("Enter index to change (-1 to quit): "))
    if index == -1:
        break
    new_value = int(input("Enter new value: "))
    numbers[index] = new_value
    print(numbers)
