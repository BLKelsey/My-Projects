import random

def word_generator(characters: str, length: int, amount: int):

    words_generated = 0                  # Counter to track how many words we've yielded
    while words_generated < amount:      # Keep generating words until we reach the required amount
        word = ''                        # Start with an empty string for the current word
        for i in range(length):          # Build the word by selecting 'length' characters
            random_char = random.choice(characters)  # Pick one random character from the provided string
            word += random_char          # Add the chosen character to the word
        yield word                       # Yield the completed word
        words_generated += 1             # Increment the counter after yielding

# Example usage
words = word_generator("apple", 4, 5)
for word in words:
    print(word)