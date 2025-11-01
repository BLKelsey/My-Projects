# Please write a function named length_of_longest, which takes a list of strings as its argument.
# The function returns the length of the longest string

def length_of_longest(my_list):
    longest_word = ''                # start with an empty string
    longest_length = 0               # keep track of the max length found so far

    for item in my_list:
        length = len(item)           # find the length of the current word
        if length > longest_length:  # check if it's longer than the longest so far
            longest_word = item      # update longest word
            longest_length = length  # update longest length
    return longest_word, longest_length

word, length = length_of_longest(["first", "second", "fourth", "eleventh"])
#word, length = length_of_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"])

print("The word that is longest is", word, '-', length, "letters")










