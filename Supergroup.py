class SuperGroup:
    def __init__(self, name, location):                 # Constructor: runs when a new SuperGroup is created
        self._name = name                               # Protected attribute for the group's name
        self._location = location                       # Protected attribute for the group's location
        self._members = []                              # Start with an empty list of heroes in the group

    def get_name(self):                                 # Getter method for the group's name
        return self._name                               # Return the name stored in _name

    def get_location(self):                             # Getter method for the group's location
        return self._location                           # Return the location stored in _location

    def add_member(self, hero):                         # Add a SuperHero object to the member list
        self._members.append(hero)                      # Append hero to _members list

    def print_group(self):                              # Print group info and its members
        print(f"Supergroup: {self._name}, {self._location}")   # Print the group's name and location
        print()
        print("Members:")                               # Print heading for members
        for hero in self._members:                      # Loop through each hero in the list
            print(hero)                                 # Print each hero (uses __str__ method of SuperHero)

# Example SuperHero class (for testing) ------------------------------------
class SuperHero:
    def __init__(self, name, powers):                   # Constructor: runs when a SuperHero is created
        self._name = name                               # Protected attribute for hero's name
        self._powers = powers                           # Protected attribute for hero's powers

    def __str__(self):                                  # Converts the object to a readable string
        return f"{self._name} - {self._powers}"         # Format: Name - Powers

# Create some heroes -------------------------------------------------------
superperson = SuperHero("SuperPerson", "super power: Superspeed, superstrength")  # Create first hero
invisible = SuperHero("Invisible Inca", "super power: Invisibility")               # Create second hero

# Create the group ---------------------------------------------------------
revengers = SuperGroup("Revengers", "Emerald City")     # Create a new SuperGroup named Revengers

# Add members to the group -------------------------------------------------
revengers.add_member(superperson)                       # Add SuperPerson to the group
revengers.add_member(invisible)                         # Add Invisible Inca to the group

# Print the group ----------------------------------------------------------
revengers.print_group()                                 # Display group name, location, and members
