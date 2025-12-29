continue_program = 'y'                        # Initializes the control variable to keep the ATM menu running

while continue_program == 'y':                 # Runs the menu repeatedly while the user chooses to continue
    print(" Choice 1: Withdraw money")         # Displays option to withdraw money
    print(" Choice 2: Deposit money")          # Displays option to deposit money
    print(" Choice 3:  Balance")               # Displays option to view account balance
    print()                                    # Prints a blank line for better readability

    choice = int(input("Enter your ATM choice: "))  # Prompts the user to enter a menu selection

    if choice == 1:                           # Checks if the user selected withdrawal
        print("How much money would you like to withdraw? ")
    elif choice == 2:                         # Checks if the user selected deposit
        print("How much money would you like to deposit? ")
    elif choice == 3:                         # Checks if the user selected balance inquiry
        print("You have chosen to see your balance")
    else:
        print("!!!  INVALID CHOICE  !!!")               # Handles any input outside the valid menu options

    continue_program = input("Would you like to continue? (y/n): ")  # Asks the user whether to continue using the ATM

print("====> PLEASE TAKE YOUR ATM CARD <====") # Displays a closing message when the user exits the program
