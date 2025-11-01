import math

def square_roots(numbers): return [math.sqrt(n) for n in numbers]  # Return list of square roots using list comprehension

lines = square_roots([1,2,3,4])  # Call the function with a list of numbers
for line in lines: print(line)  # Print each square root on a new line
