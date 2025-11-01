# Please write a function named no_vowels, which takes a string argument.
# The function returns a new string, which should be the same as the original but with all vowels removed.

def no_vowels(s):
    result = ''
    for char in s:
        if char not in "aeiou":
            result += char
    return result

print()
s = 'this is an example'
print('s = "this is an example"')
s_new = no_vowels(s)
print('s_new without vowels: ', s_new)
