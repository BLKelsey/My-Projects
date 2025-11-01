# Please write a function named words(n: int, beginning: str), which returns a list containing n random words from the words.txt file.
# All words should begin with the string specified by the second argument.
# The same word should not appear twice in the list.
# If there are not enough words beginning with the specified string, the function should raise a ValueError exception.

import random

def words(n: int, beginning: str):
    # Open the file "words1.txt" in read mode
    with open('words1.txt', 'r', encoding='utf-8-sig') as file:
        lines = file.readlines()  # Read all lines into a list

    matching_words = []  # Empty list to hold words that match

    # Go through each word in the file
    for word in lines:
        word = word.strip()  # Remove spaces and newlines
        if word.lower().startswith(beginning.lower()):
            # If the word starts with the given beginning letters
            matching_words.append(word)  # Add it to the list

    # If there are not enough words, stop with an error
    if len(matching_words) < n:
        raise ValueError("Not enough words available")

    # Sort the words alphabetically and return only the first n
    return sorted(matching_words)[:n]


# Function call
word_list = words(3, 'ca')   # Get 3 words starting with "ca"
print()
for word in word_list:
    print(word)              # Print each word on its own line







