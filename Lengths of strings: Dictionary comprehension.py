def lengths(strings: list):
    return {word: len(word) for word in strings}    # create a dictionary where each word is the key
                                                    # and its length (number of characters) is the value


word_list = ["once", "upon", "a", "time", "in"]
word_lengths = lengths(word_list)
print()
print(word_lengths)
