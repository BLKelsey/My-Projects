# Please write a program which asks the user to type in some text.
# Your program should then perform a spell check, and print out feedback to the user, so that all misspelled words have stars around them.

# Ask the user for input
sentence = input("Write text: ")

# Load dictionary words into a list
dictionary = []
with open("wordlist.txt", encoding="utf-8-sig") as new_file:
    for line in new_file:
        word = line.strip().lower()
        if word:
            dictionary.append(word)

def looks_like_misspelling(word, dictionary):
    """Check if word could be a misspelling of a dictionary word."""
    for w in dictionary:
        if len(w) == len(word):  # only compare words of same length
            # count matching characters
            matches = sum(1 for a, b in zip(word, w) if a == b)
            if matches >= len(w) - 1:   # allow 1 wrong letter
                return True
    return False

# Build checked sentence
checked_sentence = ""
for word in sentence.split():
    lw = word.lower()
    if lw in dictionary:                       # correct word
        checked_sentence += word + " "
    elif looks_like_misspelling(lw, dictionary):  # close enough → misspelled
        checked_sentence += "*" + word + "* "
    else:                                      # completely unknown word
        checked_sentence += word + " "

print(checked_sentence.strip())











