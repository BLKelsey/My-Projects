# Please write a program which asks the user for words.
# If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.


words_seen = []  # use a list to store words we've seen so far

while True:
    word = input("Enter a word: ")

    if word in words_seen:       # checks whether the current input (word) is already stored in the words_seen list.
                                 # if it IS found, that means the word has been entered before — it’s a duplicate.
                                 # if it ISN'T’t found, the word is new and will be added to the list.
                                 
        print(len(words_seen), "different words typed in.")      # len(words_seen) counts how many unique words are in the list so far.
        break
    else:
        words_seen.append(word)  # add the new word to the list



