# Please write a function named oldest_person(people: list), which takes a list of tuples as its argument.
# In each tuple, the first element is the name of a person, and the second element is their year of birth.
# The function should find the oldest person on the list and return their name.

def oldest_person(people: list):
    oldest = people[0]                 # Start by assuming the first person is the oldest

    for person in people:             # Go through each person in the list

        if person[1] < oldest[1]:       # person[1] is their year of birth: If this person was born earlier (smaller year), they are older
            oldest = person

    return oldest[0]

def older_people(people: list, year: int):
    result = []                                   # this will hold the names of people born before the given year
    for person in people:
        name = person[0]                          # first element is the name
        birth_year = person[1]                    # second element is the year of birth

        if birth_year < year:                    # check if born before the given year
            result.append(name)                  # add their name to the result list

    return result

# Example of the function in action
print()
p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

print(oldest_person(people))
print(older_people(people, 1985))

