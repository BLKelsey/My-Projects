# Please write a function named list_sum which takes two lists of integers as arguments.
# The function returns a new list which contains the sums of the items at each index in the two original lists.
# You may assume both lists have the same number of items.

def list_sum(list1, list2):
    new_list = []
    for num in range(len(list1)):                   # go through indexes
        new_list.append(list1[num] + list2[num])    # add numbers at the same index
    return new_list

print()
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
result = list_sum(list1, list2)
print(result)




