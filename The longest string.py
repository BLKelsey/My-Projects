# Please write a function named longest(strings: list), which takes a list of strings as its argument.
# The function finds and returns the longest string in the list. You may assume there is always a single longest string in the list

def longest(strings:  list) -> str:     # strings: a list means (expected to be a list of strings)
                                        # return type "-> str" means this function will return the longest string in the list
    longest = ''                        # start with an empty string as the "current longest" and ensures the first real string will replace it
    for string in strings:
        if len(string) > len(longest):  # if the current string is longer than what we have stored
            longest = string            # update "longest" to this string
    return longest

if __name__ == '__main__':
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print()
    print('Out of the list of',strings)
    print()
    print(longest(strings),'is the longest string')

