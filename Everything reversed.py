# Please write a function named everything_reversed, which takes a list of strings as its argument.
# The function returns a new list with all the items on the original list reversed.
# Also, the order of items should be reversed on the new list.

def everything_reversed(mylist):
    new_list = [word[::-1] for word in mylist[::-1]]    # create a new list by looping through the original list in reverse order
                                                        # for each word, also reverse the characters
    return new_list

# main program
mylist = ["Hi", "there", "example", "one more"]         # original list of words
print()
print(f'Normal: {mylist}')
new_list = everything_reversed(mylist)                 # call the function 'everything_reversed'
                                                       # this reverses the order of the list and also reverses each word's letters
print(f'Reversed: {new_list}')


