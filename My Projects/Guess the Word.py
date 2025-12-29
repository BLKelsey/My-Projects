secret_word = "aquarium"                              # Stores the hidden word the player must guess
guessed_letters = []                                  # Keeps track of all letters the user has guessed
display_word = "_" * len(secret_word)                 # Creates a masked version of the word using underscores

while display_word != secret_word:                    # Continues looping until the word is fully guessed
    print("Current word:", " ".join(display_word))    # Displays the current guessed state of the word
    print("Guessed letters:", ", ".join(guessed_letters))  # Shows all letters guessed so far

    guess = input("Guess a letter: ").lower()          # Prompts the user to guess a single letter and converts it to lowercase

    if guess in guessed_letters:                       # Checks if the letter was already guessed
        print("You already guessed that letter!\n")    # Informs the user of the duplicate guess
        continue                                       # Skips to the next loop iteration

    guessed_letters.append(guess)                      # Adds the new guessed letter to the list

    if guess in secret_word:                           # Checks if the guessed letter is in the secret word
        new_display = ""                               # Prepares a new version of the display word

        for i in range(len(secret_word)):                          # Loops through each letter position in the secret word
            if secret_word[i] == guess or display_word[i] != "_":  # Reveals correct guesses or keeps previous ones
                new_display += secret_word[i]                      # Adds the correct letter to the display
            else:
                new_display += "_"                     # Keeps an underscore for unguessed letters

        display_word = new_display                     # Updates the displayed word with new correct guesses
        print("Correct guess!\n")                      # Confirms a correct guess to the user
    else:
        print("Incorrect guess!\n")                    # Informs the user the guess was wrong

print("Congratulations, you guessed the word!: ",(secret_word))       # Final message shown when the word is fully guessed
