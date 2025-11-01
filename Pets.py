class Pets:                                           # Define class Pets
    def __init__(self, name, species):                # Constructor with pet's name and species
        self.name = name                              # Store pet's name
        self.species = species                        # Store pet's species

class Person:                                         # Define class Person
    def __init__(self, name, pet):                    # Constructor with person's name and their pet
        self.name = name                              # Store person's name
        self.pet = pet                                # Store reference to the Pet object

    def __str__(self):                                # Define how Person is printed
        return f"{self.name}, whose pal is {self.pet.name}, a {self.pet.species}"  # Format string with person's name and pet details

hulda = Pets("Hulda", "mixed-breed dog")         # Create a Pet object
levi = Person("Levi", hulda)                            # Create a Person object with pet Hulda
print()                                                       # Print a blank line
print(levi)                                       # "Levi, whose pal is Hulda, a mixed-breed dog"   # Print person info (calls __str__)
