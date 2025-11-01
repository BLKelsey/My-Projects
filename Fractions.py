# Write a function named fractionate(amount: int), which takes the number of parts as its argument.
# The function should divide the number 1 into as many equal-sized fractions as is specified by the argument, and return these in a list.

from fractions import Fraction

# Function that splits 1 into 'amount' equal fractions
def fractionate(amount: int):
    parts = []                              # create an empty list
    for i in range(amount):                 # repeat 'amount' times
        parts.append(Fraction(1, amount))   # add one fraction into the list
    return parts                            # return the completed list

print()
for p in fractionate(3):   # Print one fraction at a time (expected: 1/3, 1/3, 1/3)
    print(p)

print()

print(fractionate(5))     # Print the entire list returned by fractionate(5)
