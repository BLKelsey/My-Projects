# Please write an improved version of your password generator. The function now takes three arguments:
#
# If the second argument is True, the generated password should also contain one or more numbers.
# If the third argument is True, the generated password should also contain one or more of these special characters: !?=+-().

import random
import string

def generate_strong_password(length, use_numbers=True, use_specials=True):
    # start with lowercase letters
    possible_characters = string.ascii_lowercase

    # add digits if use_numbers is True
    if use_numbers:
        possible_characters += string.digits

    # add special characters if use_specials is True
    if use_specials:
        possible_characters += "!?=+-#()&"

    strpswd = ""  # start with empty string

    for i in range(length):
        strpswd += random.choice(possible_characters)  # pick from pool

    return strpswd

# Function calls
print()
for i in range(10):
    print(generate_strong_password(8, True, True))
