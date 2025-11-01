def begin_with_vowel(words: list):
    return [word for word in words  # loop through each word in the list
            if word.lower().startswith(('a', 'e', 'i', 'o', 'u'))]   # keep the word if it starts with any vowel (case-insensitive)
                                                                     # outer parentheses → belong to the startswith() function call
                                                                     # inner parentheses → define a tuple of vowels ('a','e','i','o','u')
print()
words = ["automobile","motorbike","Animal","cat","Dog","APPLE","orange"]
for vowelled in begin_with_vowel(words):
    print(vowelled)




