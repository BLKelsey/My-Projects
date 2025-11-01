class Money:                           # Define a class named Money
    def __init__(self, dollars, cents): # Constructor: runs when a new Money object is created
        self.dollars = dollars          # Store the dollar part in an instance variable
        self.cents = cents              # Store the cents part in an instance variable

    def __str__(self):                  # Define how the object is displayed when printed
        return f"{self.dollars}.{self.cents:02d} dollars"    # Format cents with two digits (e.g., 05 instead of 5)

    def __eq__(self, another):  # Define how to compare two Money objects for equality
        return self.dollars == another.dollars and self.cents == another.cents  # Returns True only if both dollars and cents are the same


dc1 = Money(4, 10)
dc2 = Money(2, 5)
dc3 = Money(4, 10)

print()
print(dc1)
print(dc2)
print(dc3)
print(dc1 == dc2)
print(dc1 == dc3)
