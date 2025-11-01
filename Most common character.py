# Please write a function named most_common_character, which takes a string argument.
# The function returns the character which has the most occurrences within the string.
# If there are many characters with equally many occurrences, the one that appears first in the string should be returned.

def most_common_character(s):
    most_common = ""
    highest_count = 0

    for char in s:                       # check every character in the string
        count = s.count(char)            # count how many times it appears
        if count > highest_count:        # update if this is the new highest
            most_common = char
            highest_count = count
    return most_common, highest_count


s = 'abcdbde'
s2 = 'exemplary elementary'

# function calls
char1, count1 = most_common_character(s)
char2, count2 = most_common_character(s2)

print(s, "-", char1, "(", count1, "times )")
print(s2, "-", char2, "(", count2, "times )")



