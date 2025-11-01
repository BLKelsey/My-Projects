# Please write a phone book application


phone_book = {}   # Start with an empty dictionary

while True:
    print("\nEnter '1' to search, '2' to add or '3' to quit: ")
    user = input("Enter your choice: ")

    if user == '1':   # Search
        name = input("Enter name to search: ")
        if name in phone_book:
            print(f"{name}: {phone_book[name]}")
        else:
            print(f"{name} not found.")

    elif user == '2':  # Add
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        phone_book[name] = number   # Add to dictionary
        print(f"{name} added with number {number}.")
        print("OK!")

    elif user == '3':  # Quit
        print("Goodbye!")
        break
