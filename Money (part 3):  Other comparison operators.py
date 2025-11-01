class Money:                           # Define a class named Money
    def __init__(self, dollars, cents): # Constructor: runs when a new Money object is created
        self.dollars = dollars          # Store the dollar part in an instance variable
        self.cents = cents              # Store the cents part in an instance variable

    def __str__(self):                  # Define how the object is displayed when printed
        return f"{self.dollars}.{self.cents:02d} dollars"    # Format cents with two digits (e.g., 05 instead of 5)

    def __gt__(self, another):            # defines behavior for '>' operator (greater than)
        return self.dollars > another.dollars  # returns True if this object's dollars is greater

    def __lt__(self, another):            # defines behavior for '<' operator (less than)
        return self.dollars < another.dollars  # returns True if this object's dollars is smaller

    def __ne__(self, another):            # defines behavior for '!=' operator (not equal)
        return self.dollars != another.dollars  # returns True if dollar values are not equal

dc1 = Money(4, 10)
dc2 = Money(2, 5)

print()
print(dc1 != dc2)
print(dc1 < dc2)
print(dc1 > dc2)
