class Person:
    def __init__(self, name, height):                     # Constructor: takes a name and height
        self.name = name                                  # Store the person's name
        self.height = height                              # Store the person's height (in inches)

class Room:                                               # Class to represent a room with people inside
    def __init__(self, persons=None):                     # Constructor: optional list of people
        if persons is None:                               # If no list was given
            persons = []                                  # Start with an empty list
        self.persons = persons                            # Save the list of people in the room

    def add(self, person):                                # Method to add a new person
        self.persons.append(person)

    def is_empty(self):                                   # Check if room has no people
        return not self.persons                           # Returns True if empty, False otherwise

    def print_contents(self):                             # Print details about the room
        if self.is_empty():                               # If the room has no people
            print("The room is empty.")                   # Print empty message
        else:                                             # Otherwise, show details
            total_height = sum(person.height for person in self.persons)  # Sum all heights
            print(f"There are {len(self.persons)} persons in the room, "
                  f"and their combined height is {total_height} inches")  # Print count + total height
            for person in self.persons:                                    # Loop through each person
                print(f"{person.name} ({person.height} inches)")           # Print name + height

room = Room()                                             # Create an empty room
print()
print("Is the room empty?", room.is_empty())              # First check → should print True
room.print_contents()                                     # Show message that room is empty

# Add people to the room
room.add(Person("Lea", 72))
room.add(Person("Kenya", 67))
room.add(Person("Ally", 65))
room.add(Person("Nina", 64))
room.add(Person("Dorothy", 61))

print("Is the room empty?", room.is_empty())              # Second check → should print False
room.print_contents()                                     # Show number of people, combined height, and details
