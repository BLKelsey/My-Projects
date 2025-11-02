def most_common_words(filename, lower_limit):
    # Open the file safely for reading
    with open(filename, "r") as file:
        # Read all text, convert to lowercase, and replace punctuation with spaces
        text = file.read().lower()

    # Remove basic punctuation by replacing them with spaces
    for punct in [".", ",", ":", ";", "!", "?", "(", ")", '"', "'"]:
        text = text.replace(punct, " ")

    # Split text into words
    words = text.split()

    # Count how many times each word appears (dictionary comprehension)
    word_counts = {word: words.count(word) for word in set(words)}

    # Filter out words that appear fewer than lower_limit times
    result = {word: count for word, count in word_counts.items() if count >= lower_limit}
    return result

# Example call using your file
print()
print(most_common_words("comprehension.txt", 3))
