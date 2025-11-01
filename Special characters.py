# The Python module string contains some string constants, which define certain groups of characters.
# These include for example lowercase letters and punctuation characters.
# Please familiarize yourself with these constants, and then write a function named separate_characters(my_string: str).
# The function takes a string as its argument, and it should separate the characters in the string into three other strings, and return these in a tuple


import string

def separate_characters(my_string: str):

    # Create empty strings for each category
    letters = ""
    punctuations = ""
    others = ""

    for char in my_string:
        if char in string.ascii_letters:
            letters += char                # add to the letters string
        elif char in string.punctuation:
            punctuations += char          # add to the punctuations string
        else:                             # If the character is anything else (numbers, spaces, accented letters, etc.)
            others += char                # add to the others string
    return letters, punctuations, others


# Test
parts = separate_characters("H3y! Is my son is w0rking l@te!?")
print('ASCII Letter: ',parts[0])    # letters
print('Punctuation: ',parts[1])     # punctuation
print('Others: ',parts[2])         # others



