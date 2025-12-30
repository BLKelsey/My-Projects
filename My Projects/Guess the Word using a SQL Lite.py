import sqlite3                                  # Import SQLite support (built into Python)
import random                                   # Import random module (used by SQLite RANDOM())

# Connect to (or create) the database file
conn = sqlite3.connect("SecretWords.db")        # Opens SecretWords.db or creates it if it doesn't exist
cursor = conn.cursor()                          # Creates a cursor TO RUN SQL commands

# Create the table
cursor.execute("""                              -- Executes a SQL command
CREATE TABLE IF NOT EXISTS SecretWords (        -- Creates table ONLY IF it does not already exist
    id INTEGER PRIMARY KEY AUTOINCREMENT,       -- Auto-incrementing ID for each word
    word TEXT NOT NULL                          -- Column to store the secret word
)
""")

# Insert some secret words
words = ["aquarium", "membership", "components", "guidelines",
         "investments", "professionalism", "compensation"]   # List of words to store in the database

for word in words:                                 # Loop through each word
    cursor.execute("INSERT INTO SecretWords (word) VALUES (?)",
                   (word.lower(),))                # Insert each word (stored in lowercase)

# Save changes and close
conn.commit()                                   # Saves all inserts to the database file
conn.close()                                    # Closes the database connection

print("Database created and words added.")      # Confirms database setup

# Connect to database
conn = sqlite3.connect("SecretWords.db")        # Reopen the database for gameplay
cursor = conn.cursor()                          # Create a new cursor

# Get one random word
cursor.execute("SELECT word FROM SecretWords ORDER BY RANDOM() LIMIT 1")  # Pick one random word
secret_word = cursor.fetchone()[0]              # Extract the word from the query result

conn.close()                                    # Close database (no longer needed)

guessed_letters = []                            # List to store letters the user has guessed
display_word = "*" * len(secret_word)           # Masked version of the secret word

while display_word != secret_word:              # Loop until the word is fully guessed
    print("Current word:", " ".join(display_word))  # Show masked word with spaces
    print("Guessed letters:", ", ".join(guessed_letters))  # Show guessed letters

    guess = input("Guess a letter: ").lower()   # Ask user for a letter and convert to lowercase

    if guess in guessed_letters:                # Check if letter was already guessed
        print("You already guessed that letter!\n")
        continue                                # Skip to next loop iteration

    guessed_letters.append(guess)               # Store the new guessed letter

    if guess in secret_word:                    # Check if the guess is correct
        new_display = ""                        # Build updated display word
        for i in range(len(secret_word)):       # Loop through each letter position
            if secret_word[i] == guess or display_word[i] != "*":
                new_display += secret_word[i]   # Reveal correct letters
            else:
                new_display += "*"              # Keep masked letters hidden
        display_word = new_display              # Update the display word
        print("Correct guess!\n")
    else:
        print("Incorrect guess!\n")             # Guess was not in the word

print("Congratulations, you guessed the word:", secret_word)  # Game completion message
