# Please write a program which asks the user to type in a string.
# The program then prints each input character on a separate line.
# After each character, there should be a star (*) printed on its own line.

string = input('Please type in a word: ')
print(string)
for char in string:
    print(char)
    print ('*')



