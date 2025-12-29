import random                                           # Imports the random module

def play_game(secret_number):                           # Defines the guessing game function
    guess = 0                                           # Stores the user's current guess
    guess_count = 0                                     # Counts how many guesses are made

    while guess != secret_number:                        # Loop continues until the correct number is guessed
        guess = int(input("Guess a number between 1 and 10: "))  # Gets the user's guess
        guess_count += 1                                # Increases the guess counter by one

        if guess < secret_number:                        # Checks if the guess is too low
            print("Too low")                             # Informs the user
            print()
        elif guess > secret_number:                      # Checks if the guess is too high
            print("Too high")                            # Informs the user
            print()
        else:                                            # Runs when the guess is correct
            print("CORRECT...it took you", guess_count, "guesses.")  # Success message

secret_number = random.randint(1, 10)                   # Generates a random number between 1 and 10
play_game(secret_number)                                # Starts the game
