class Rectangle:                                      # Define a class for rectangles
    def __init__(self, width, height):                # Constructor with width and height
        self.width = width                            # Store the width of the rectangle
        self.height = height                          # Store the height of the rectangle

    def area(self):                                   # Method to calculate area
        return self.width * self.height               # Multiply width × height and return result

    def __str__(self):                                        # Method to return a string version of the object
        return f"Rectangle: ({self.width} x {self.height})"   # Show rectangle dimensions

class Square(Rectangle):                              # Define a class Square that INHERITS from Rectangle
    def __init__(self, side):                         # Constructor for square (only one side needed)
        super().__init__(side, side)                  # Call Rectangle constructor with both sides equal

if __name__ == "__main__":                            # Run this block only if file executed directly
    square = Square(4)                                # Create a Square object with side length 4
    print()                                           # Print a blank line for spacing
    print(square)                                     # Print string output from __str__()
    print("area:", square.area())                     # Print area calculated from Rectangle’s method
