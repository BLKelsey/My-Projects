# Please write three functions: first_word, second_word and last_word. Each function takes a string argument.

def first_word(sentence):
    return sentence.split()[0]    #.split() takes the string in sentence and splits it into a list of words.
                                  # by default, .split() uses whitespace (spaces, tabs, newlines) as the separator.
                                  # Example: "it was a dark and stormy night".split()
                                      #  → ['it', 'was', 'a', 'dark', 'and', 'stormy', 'night']

def second_word(sentence):
    return sentence.split()[1]

def last_word(sentence):
    return sentence.split()[-1]


# Example usage
sentence = "it was a dark and stormy night"

print(first_word(sentence))   # it
print(second_word(sentence))  # was
print(last_word(sentence))    # night
