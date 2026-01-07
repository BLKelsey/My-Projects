while True:
    user_input = input("Enter some text: ")

    if user_input != "":
       break
    else:
        print("You must enter something. Please try again.")
        print()

print( "Thank you. You entered: " + user_input)

