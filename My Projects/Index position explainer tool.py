items = [
    "Apple",
    "Swimming Pool",
    "Yellow",
    "Television",
    "Stovetop",
    "Bottle",
    'Barstool',
    "Construction",
    "Outdoors",
    "Gym",
    "Nuclear",
    "Pantry"
]
display_number = 1                     # Start numbering at 1 for human-friendly display

print("Here are the items:")           # Print a heading for the list

for item in items:                     # Loop through each item in the list
    print(display_number, ".", item)   # Display the number and the current item
    display_number += 1                # Increase the number after each item

print("Choose an item number:")         # Ask the user to choose an item
user_number = int(input("> "))          # Get user input and convert it to an integer
index_pos = user_number - 1             # Convert the user's number choice (starts at 1) to a list index which actually (starts at 0)

if index_pos < 0 or index_pos >= len(items):   # Check if index is out of range
    print("That number is out of range")        # Warn the user
else:
    print("You chose item number:", user_number)       # Confirm user's choice
    print()
    print("In Python: THIS item is at INDEX: ==>", index_pos)  # Explain the index
    print("The item is: ==> ", items[index_pos])     # Display the selected item