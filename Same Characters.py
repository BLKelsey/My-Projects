# Please write a function named same_chars, which takes one string and two integers as arguments.
# The integers refer to indexes within the string. The function should return True if the two characters at the indexes specified are the same.
# Otherwise, and especially if either of the indexes falls outside the scope of the string, the function returns False

def same_chars(string, index1, index2):
    if string[index1] == string[index2]:
        return True
    else:
        return False
print(same_chars("television", 0, 1))
print(same_chars("programmer", 3, 7))
print(same_chars("university", 6, 6))