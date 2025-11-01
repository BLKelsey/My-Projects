# Please write a function named all_the_longest, which takes a list of strings as its argument.
# The function should return a new list containing the longest string in the original list.
# If more than one are equally long, the function should return all of the longest strings.
# The order of the strings in the returned list should be the same as in the original.

def all_the_longest(my_list):
    longest_words = []     # list to store all longest words
    longest_length = 0     # track the maximum length found so far

    for item in my_list:
        length = len(item)
        if length > longest_length:         # found a new longest word
            longest_length = length
            longest_words = [item]          # start a new list with this word
        elif length == longest_length:      # tie: same length as longest
            longest_words.append(item)      # add to the list of longest words

    return longest_words, longest_length

#word, result = all_the_longest(["first", "second", "fourth", "eleventh"])
word, result = all_the_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"])

print('Longest word(s) in list =', word, '-', result, "letters")










