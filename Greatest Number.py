# Please write a function named greatest_number, which takes three arguments.
# The function returns the greatest in value of the three.

def greatest_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    elif c > a and c > b:
        return c
    else:
        return 0


result = greatest_number
print(greatest_number(3, 4, 1))
print(greatest_number(99, -4, 7))
print(greatest_number(0, 0, 0))

