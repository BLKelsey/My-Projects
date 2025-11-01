def read_input():
    while True:
        print()
        choice = input("Please enter an integer between 5 and 10: ")

        # Check if input is digits only
        if not choice.isdigit():
            print("Invalid choice, try again. You must type an integer between 5 and 10")
            continue   # go back to the top of the loop

        # Safe to convert now
        choice = int(choice)

        if choice < 5 or choice > 10:
            print("Invalid choice, try again. You must type an integer between 5 and 10")
        else:
            print(f"You typed: {choice}")
            break   # exit loop after valid input
# ✅ Call the function
read_input()









