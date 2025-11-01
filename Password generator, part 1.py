# Please write a function which creates passwords of a desired length, consisting of lowercase characters a to z.

import random
import string

def generate_password(length: int):
    letters = string.ascii_lowercase     # all lowercase letters
    password = ''                        # start with empty string

    for i in range(length):                 # repeat 'length' times
        password += random.choice(letters)  # add one random letter each time

    return password

# Function calls
print()
for i in range(10):                      # repeat 10 times
    print(generate_password(8))          # generate and print an 8-letter password





