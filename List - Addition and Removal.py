# Please write a program which asks the user to choose between addition and removal.
# Depending on the choice, the program adds an item to or removes an item from the end of a list.
# The item that is added must always be one greater than the last item in the list. The first item to be added must be 1.


numbers = []  # don't name it "list", that overwrites Python's built-in list type

while True:  # loop until user chooses to exit
    choice = input("Select your choice: (a) add, (r) remove, (x) exit: ")

    if choice == "a":
        value = input("Enter a number to add: ")
        numbers.append(value)
        print(numbers)

    elif choice == "r":
        value = input("Enter a number to remove: ")
        if value in numbers:
            numbers.remove(value)
        else:
            print("Value not found.")
        print(numbers)

    elif choice == "x":
        break  # now this is valid because it's inside a loop

    else:
        print("Invalid choice. Try again.")
print('Bye!')