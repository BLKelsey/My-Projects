# Please write a function named hypotenuse(leg1: float, leg2: float), which takes the lengths of the two sides
# adjacent to the right angle of an orthogonal triangle. The function should return the length of the hypotenuse, or the side opposite to the right angle.

# You can use the Pythagorean theorem to calculate the result. You will need the sqrt function from the math module.

from math import sqrt
def hypotenuse(leg1: float, leg2: float):

    # Step 1: Square both legs
    square1 = leg1 * leg1
    square2 = leg2 * leg2

    # Step 2: Add the squares together
    sum_of_squares = square1 + square2

    # Step 3: Take the square root of the sum
    hypotenuse_length = sqrt(sum_of_squares)

    # Step 4: Return the result
    return hypotenuse_length

result = hypotenuse(leg1=3, leg2=7)
result1 = hypotenuse(leg1=5, leg2=9)
print()
print('The hypootenuse "bottom size of triangle" of 3 and 7 =',result)
print('The hypotenuse  "bottom size of triangle" of 13 and7 7 =',result1)

