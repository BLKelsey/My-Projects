def calculate(celsius):                                    # Defines a function that converts a Celsius temperature to Fahrenheit
    return (celsius * 9 / 5) + 32                          # Applies the Celsius → Fahrenheit formula and returns the result

while True:                                                # Starts an infinite loop so the program can run repeatedly
    answer = input("Choose a number in Celsius you want to convert to Fahrenheit (or q to quit): ")  # Prompts the user for input
    print()                                                 # Prints a blank line for cleaner output formatting

    if answer == "q":                                      # Checks if the user wants to quit
        print("Thank you for using my Celsius to Fahrenheit converter, goodbye!")  # Displays a farewell message
        break                                               # Exits the loop and ends the program

    user_input = float(answer)                             # Converts the user’s input from text to a floating-point number so both integers and decimal temperatures are accepted
    fahrenheit = calculate(user_input)                     # Calls the calculate function to convert Celsius to Fahrenheit

    print("That is", fahrenheit, "degrees Fahrenheit")     # Displays the conversion result
    print("Type 'q' to quit")                              # Informs the user how to exit the program
