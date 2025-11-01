# Please define the class Pet.
# The class should include a constructor, which takes the initial values of the attributes name, species and year_of_birth as its arguments, in that specific order.
#
# Please also write a function named new_pet(name: str, species: str, year_of_birth: int) outside the class definition.
# The function should create and return a new object of type Pet, as defined in the class Pet.

class Pet:

    # Constructor method, runs when a new Pet object is created
    def __init__(self, name,species,year_of_birth):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth

# Define a function (outside the class) that creates a new Pet object
def new_pet(name: str, species: str, year_of_birth: int):
        pet = Pet(name, species, year_of_birth)                   # create a new Pet object using the class
        return pet

fluffy = new_pet("Fluffy", "Dog", 2017)
print()
print(fluffy.name)
print(fluffy.species)
print(fluffy.year_of_birth)
