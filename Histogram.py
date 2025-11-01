# Please write a function named histogram, which takes a string as its argument.
# The function should print out a histogram representing the number of times each letter occurs in the string. Each occurrence of a letter should be represented by a star on the specific line for that letter.
#
# For example, the function call histogram("statistically") should print out

def histogram(word):
    counts = {}                        # Dictionary to store character counts and how many times each character appears
    for char in word:                  # Loop through each character in the given word
        if char in counts:             # If we've seen this character before
            counts[char] += 1          # Increase its count
        else:                          # If it's the FIRST time we've seen it
            counts[char] = 1           # Start count at 1

    for char, count in counts.items():  # loop through each (key, value) pair in the dictionary
                                        # store the key in char and the value in count

        print(char, "*" * count)        # print character and stars

if __name__ == '__main__':
   histogram('statistically')



