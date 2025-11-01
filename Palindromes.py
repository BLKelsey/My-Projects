# Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome.
# Palindromes are words that are spelled exactly the same backwards and forwards.
# Please also write a main program which asks the user to type in words until they type in a palindrome.

def palindromes(word):
   return word == word[::-1]

while True:
    word = input("Please type in a word: ")
    if palindromes(word):
        print("That word is a palindrome!")

    else:
        print("That word was not a palindrome.")


