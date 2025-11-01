
class Person:                                  # Define a class called Person
    def __init__(self, name: str):             # Constructor method, runs when a new Person is created
        self.name = name                       # Store the person's full name in the attribute 'name'

    def return_first_name(self):               # Method to get the first name
        parts = self.name.split(" ")           # Split the full name into parts (separated by spaces)
        return parts[0]                        # Return the first part (first name)

    def return_last_name(self):                # Method to get the last name
        parts = self.name.split(" ")           # Split the full name into parts
        return parts[1]                        # Return the second part (last name)

if __name__ == "__main__":                     # This ensures the code only runs when executed directly
    peter = Person("Peter Pythons")            # Create a Person object named peter
    print(peter.return_first_name())
    print(peter.return_last_name())

    paula = Person("Paula Pythonnen")          # Create another Person object named paula
    print(paula.return_first_name())
    print(paula.return_last_name())
