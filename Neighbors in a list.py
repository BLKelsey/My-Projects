# Given a list of integers, let's decide that two consecutive items in the list are neighbors if their difference is 1.
# So, items 1 and 2 would be neighbors and so would items 56 and 55.
#
# Please write a function named longest_series_of_neighbors, which looks for the longest series of neighbors within the list, and returns its length.

def longest_series_of_neighbors(mylist):
    longest = 1      # longest series found. Even if your list has only one number, that by itself counts as a "series" of length 1.
                     # Example: [7] → the longest sequence is just [7], so length = 1.
    current = 1      # current series length
    print()
    print('Numbers seperated by 1 or -1: ')

    for i in range(1, len(mylist)):   # loop through mylist starting from index 1,so we can compare each element with the previous one
        if mylist[i] - mylist[i-1] == 1 or mylist[i] - mylist[i-1] == -1:    # Check if two numbers are neighbors (+1 or -1 apart)
                                                                             # mylist[i] = the current number in the loop.
                                                                             # mylist[i - 1] = the previous number in the loop
                                                                             # this subtracts the previous number from the current number
                                                                             # the result tells you how far apart they are
            print(mylist[i - 1], mylist[i],  'are neighbors')
            current += 1        # continue the series
            if current > longest:
                longest = current
        else:
            current = 1         # reset if not neighbor
    return longest

mylist = [1, 2, 5, 4, 3, 4]
print("Longest series length:", longest_series_of_neighbors(mylist))
