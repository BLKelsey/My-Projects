class Recording:
    def __init__(self, length):                 # Constructor, runs when an object is created
        self.__length = length                  # Store the given length in a PRIVATE variable

    @property
    def length(self):                           # Getter method for length
         return self.__length                   # Return the private length value

    @length.setter                              # Setter method for length
    def length(self, length):                   # Accepts a NEW LENGTH value
        self.__length = length                  # UPDATE the private length variable with new value

the_wall = Recording(43)                        # Create a Recording object with length 43
print()
print(the_wall.length)                          # CALL THE GETTER → prints 43
the_wall.length = 44                            # CALL THE SETTER → sets length to 44
print(the_wall.length)                          # CALL THE GETTER again → prints 44
