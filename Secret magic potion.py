class MagicPotion:                                   # Base class representing a simple potion recipe
    def __init__(self, name: str):                   # Constructor initializes potion name and ingredient list
        self._name = name                            # Store the name of the potion
        self._ingredients = []                       # Create an empty list to hold ingredients

    def add_ingredient(self, ingredient: str, amount: float):  # Method to add ingredients to the list
        self._ingredients.append((ingredient, amount))         # Store each ingredient and its amount as a tuple

    def print_recipe(self):                          # Method to print the potion recipe
        print(f"{self._name}:")                      # Print the potion name
        for ingredient, amount in self._ingredients: # Loop through all stored ingredients
            print(f"{ingredient} {amount} grams")    # Print each ingredient and its amount

class SecretMagicPotion(MagicPotion):                # Subclass that adds password protection to MagicPotion
    def __init__(self, name: str, password: str):    # Constructor with name and password
        super().__init__(name)                       # Call the parent constructor to set up potion name and list
        self._password = password                    # Store the password securely in an instance variable

    def add_ingredient(self, ingredient: str, amount: float, password: str):  # Override add_ingredient to require password
        if password != self._password:               # Check if entered password matches the stored one
            print("1st try: Wrong password")         # Print message if password is incorrect
        else:
            super().add_ingredient(ingredient, amount)  # Call parent method to add ingredient if password is correct

    def print_recipe(self, password: str):           # Override print_recipe to require password
        if password != self._password:               # Check the password before printing
            print("1st try: Wrong password")         # Print warning if the password is wrong
        else:
            print("2nd try (correct) password --> ", end="")  # Indicate successful password
            super().print_recipe()                   # Call parent method to print full recipe

# -----------------------------
# Main Program
# -----------------------------
print("Ingredients:")                                # Label before listing ingredients

potion = SecretMagicPotion("Diminuendo maximus", "hocuspocus")  # Create a SecretMagicPotion with a password

# Add ingredients using the correct password
potion.add_ingredient("Toadstool", 1.5, "hocuspocus")           # Add first ingredient
potion.add_ingredient("Magic sand", 3.0, "hocuspocus")          # Add second ingredient
potion.add_ingredient("Frogspawn", 4.0, "hocuspocus")           # Add third ingredient

potion.print_recipe("pocushocus")                               # Prints "1st try: Wrong password"
potion.print_recipe("hocuspocus")                               # Prints recipe successfully
