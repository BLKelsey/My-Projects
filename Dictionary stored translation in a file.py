# Start an infinite loop that runs until 'break' is used
while True:

    # Print a blank line for readability
    print()

    # Show the menu options to the user
    print("1 - add an entry, 2 - read entries, 3 - translate, 0 - quit")

    # Ask the user for their choice (1, 2, 3, or 0)
    choice = input("Function: ")

    # If user chose 1 → add a new dictionary entry
    if choice == "1":
        # Ask for Finnish word
        finnish = input("Finnish word: ")

        # Ask for English word
        english = input("English word: ")

        # Open dictionary.txt in append mode so new entries are added at the end
        with open("dictionary.txt", "a", encoding="utf-8") as dictionary:
            # Write the entry in "finnish:english" format
            dictionary.write(f"{finnish}:{english}\n")

        # Confirm entry added
        print("Dictionary entry added\n")

    # If user chose 2 → read all entries
    elif choice == "2":
        # Print header
        print("Entries:")

        # Open dictionary.txt for reading
        with open("dictionary.txt", "r", encoding="utf-8") as dictionary:
            # Go through each line in the file
            for line in dictionary:
                # Print each entry without newline characters
                print(line.strip())

        # Add a blank line after entries
        print()

    # If user chose 3 → translate a Finnish word
    elif choice == "3":
        # Ask user for a Finnish word and make it lowercase for case-insensitive matching
        search = input("Enter a Finnish word to translate: ").strip().lower()

        # Flag to track if the translation is found
        found = False

        # Open dictionary.txt for reading
        with open("dictionary.txt", "r", encoding="utf-8") as dictionary:
            # Go through each line in the file
            for line in dictionary:
                # Split the line into [finnish, english]
                parts = line.strip().split(":")

                # Only proceed if we have exactly two parts
                if len(parts) == 2:
                    # Unpack Finnish and English
                    finnish, english = parts

                    # Compare Finnish word (case-insensitive)
                    if finnish.lower() == search:
                        # Print the translation
                        print(f"{finnish} → {english}")

                        # Mark as found
                        found = True

                        # Stop searching after finding the match
                        break

        # If no match was found
        if not found:
            # Tell the user
            print("Translation not found.\n")

    # If user chose 0 → quit the program
    elif choice == "0":
        # Say goodbye
        print("Bye now!")

        # Exit the loop → program ends
        break

    # If the choice is not 1, 2, 3, or 0
    else:
        # Tell the user their input was invalid
        print("Invalid choice, try again.\n")
