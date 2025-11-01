# Please write a program which asks the user to type in values and adds them to a list.
# After each addition, the list is printed out in two different ways:
    # in the order the items were added
    # ordered from smallest to greatest
# The program exits when the user types in 0.

mylist = []

while True:
    value = int(input("Type in a value you want to add to the list (type '0' to quit):  "))
    if value == 0: break

    mylist.append(value)
    print('New item: ',value)
    print('The list now: ',mylist)
    print('The list in order: ',sorted(mylist))

