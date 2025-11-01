# PART 1:
# The Python string method isupper() returns True if a string consists of only uppercase characters.


def isupper(word):
    return word.isupper()      # returns True if all letters in word are uppercase, otherwise False

word = 'LAKELAND'
word2 = 'lakeland'

print()
print(word, "is uppercase?", isupper(word))      # function call inside print statements
print(word2, "is uppercase?", isupper(word2))


# PART 2:
# Please use the isupper method to write a function named no_shouting, which takes a list of strings as an argument.
# The function returns a new list, containing only those items from the original which do not consist of solely uppercase characters.

def no_shouting(mylist):
    result = []                      # create an empty list to store words that are not all uppercase
    for word in mylist:              # loop through each word in the list
        if not word.isupper():       # check if the word is NOT all uppercase
            result.append(word)      # if so, add it to the result list
    return result                    # return the list of non-uppercase words

print()
words = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
print('Some words are shouting: ',words)
print('Shouted words removed:  ',no_shouting(words))    # call the function and print the new list with uppercase-only words REMOVED












