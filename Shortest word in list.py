# Please write a function named shortest, which takes a list of strings as its argument.
# The function returns whichever of the strings is the shortest.
# If more than one are equally short, the function can return any of the shortest strings (there will be no such situation in the tests).
# You may assume there will be no empty strings in the list.

def shortest(my_list):
    shortest_word = my_list[0]               # start by assuming the first word is the shortest
    shortest_length = len(my_list[0])        # keep track of the min length found so far

    for item in my_list:                     # go through every word in the list
        length = len(item)                   # find the length of the current word
        if length < shortest_length:         # check if it's shorter than the shortest so far
            shortest_word = item             # update shortest word
            shortest_length = length         # update shortest length
    return shortest_word, shortest_length

word, length = shortest(["adele", "mark", "dorothy", "tim", "hedy", "richard"])
print("The word that is shortest is", word, '-', length, "letters")
