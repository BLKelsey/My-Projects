from difflib import get_close_matches
import string

def spell_checker():
    # 1. Ask the user for input
    line_of_text = input("write text: ")

    # 2. Split into words
    words = line_of_text.split()

    # 3. Prepare storage
    corrected_line = []
    suggestions = {}

    # 4. Define dictionary of correct words
    dictionary_of_correct_words = [
        "we", "use", "python", "to", "make", "a", "museful", "usefully","checker",
        "this", "is", "actually", "good", "and", "useful", "program",
        "can", "be", "hard", "sometimes"
    ]

    # 5. For each word
    for word in words:
        # remove punctuation like . , ? !
        clean_word = word.strip(string.punctuation)

        if clean_word.lower() in dictionary_of_correct_words:
            # word is correct → keep it
            corrected_line.append(word)
        else:
            # word is misspelled → enclose in stars
            corrected_line.append("*" + word + "*")

            # find close matches
            possible_words = get_close_matches(clean_word.lower(), dictionary_of_correct_words)

            # store suggestions
            suggestions[clean_word] = possible_words

    # 6. Print corrected sentence
    print(" ".join(corrected_line))

    # 7. Print suggestions
    if suggestions:
        print("suggestions:")
        for wrong_word, possible_words in suggestions.items():
            print(wrong_word + ":", ", ".join(possible_words))

# Run program
spell_checker()
