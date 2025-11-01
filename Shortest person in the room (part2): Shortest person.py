class Person:
    def __init__(self, name, height):           # Constructor: takes a name and height
        self.name = name                        # Store the person's name
        self.height = height                    # Store the person's height (in inches)

class Room:
    def __init__(self, persons=None):           # Constructor: optional list of people
        if persons is None:                     # If no list is given
            persons = []                        # Start with an empty list
        self.persons = persons                  # Save the list of people in the room

    def add(self, person):                      # Add a person to the room
        self.persons.append(person)

    def shortest(self):                         # Find the shortest person
        if self.is_empty():                     # If room is empty, return None
            return None
        shortest_person = self.persons[0]       # Start by assuming first person is shortest
        for person in self.persons:             # Check each person in the list
            if person.height < shortest_person.height:   # If someone is shorter
                shortest_person = person        # Update shortest person
        return shortest_person                  # Return the shortest person object

    def is_empty(self):                         # Check if room has no people
        return not self.persons                 # True if empty, False otherwise

    def print_contents(self):                   # Print details about the room
        if self.is_empty():                     # If the room has no people
            print("The room is empty.")         # Print empty message
        else:
            total_height = sum(person.height for person in self.persons)  # Sum all heights
            print(f"There are {len(self.persons)} persons in the room, "
                  f"and their combined height is {total_height} inches")
            for person in self.persons:                                   # Loop through each person
                print(f"{person.name} ({person.height} inches)")

room = Room()
print()
print("Is the room empty?", room.is_empty())
print("Shortest:", room.shortest())             # None since room is empty

# Add people
room.add(Person("Lea", 72))
room.add(Person("Kenya", 67))
room.add(Person("Ally", 65))
room.add(Person("Nina", 64))
room.add(Person("Dorothy", 61))

print()
print("Is the room empty?", room.is_empty())   # room is no longer empty
shortest = room.shortest()
print(f"Shortest: {shortest.name} ({shortest.height} inches)")  # Print name + height
print()
room.print_contents()
