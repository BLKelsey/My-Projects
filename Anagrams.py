# Please write a function named anagrams, which takes two strings as arguments.
# The function returns True if the strings are anagrams of each other.
# Two words are anagrams if they contain exactly the same characters.

def anagrams(word1,word2):
    return sorted(word1) == sorted(word2)   # two words are anagrams if their sorted characters are the same

print('Anagram or not?')
print()
print("tame vs meta:", anagrams("tame", "meta"))     # True
print("tame vs mate:", anagrams("tame", "mate"))     # True
print("tame vs team:", anagrams("tame", "team"))     # True
print("tabby vs batty:", anagrams("tabby", "batty")) # False
print("python vs java:", anagrams("python", "java")) # False