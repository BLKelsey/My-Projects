class Money:                           # Define a class named Money
    def __init__(self, dollars, cents): # Constructor: runs when a new Money object is created
        self.dollars = dollars          # Store the dollar part in an instance variable
        self.cents = cents              # Store the cents part in an instance variable

    def __str__(self):                  # Define how the object is displayed when printed
        return f"{self.dollars}.{self.cents:02d} dollars"    # Format cents with two digits (e.g., 05 instead of 5)

dc1 = Money(4, 10)                      # Create a Money object: 4 dollars 10 cents
dc2 = Money(2, 5)                       # Create another Money object: 2 dollars 5 cents

print()                                 # Print a blank line for spacing
print(dc1)                              # Prints: 4.10 dollars
print(dc2)                              # Prints: 2.05 dollars
