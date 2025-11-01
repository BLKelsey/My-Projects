class Money:                                   # Define a class named Money
    def __init__(self, dollars, cents):        # Constructor
        self.dollars = dollars
        self.cents = cents

    def __str__(self):                         # How to display when printed
        return f"{self.dollars}.{self.cents:02d} dollars"

    def __add__(self, another):  # Defines behavior for the + operator
        # Convert both amounts into total cents to simplify math
        total_self = self.dollars * 100 + self.cents  # Convert this Money object to cents
        total_another = another.dollars * 100 + another.cents  # Convert the other Money object to cents

        # Add both totals together (in cents)
        total_cents = total_self + total_another

        # Convert total cents back into dollars and cents
        dollars = total_cents // 100  # Integer division gives whole dollars
        cents = total_cents % 100  # Modulo gives the remaining cents (0–99)

        # Return a new Money object with the sum (do not change existing objects)
        return Money(dollars, cents)

    def __sub__(self, another):  # Defines behavior for the - operator
        total_self = self.dollars * 100 + self.cents  # Convert this Money object to cents
        total_another = another.dollars * 100 + another.cents  # Convert the other Money object to cents

        # Check if subtraction would result in a negative amount
        if total_self < total_another:
            raise ValueError("Dollars cannot be negative")  # Stop and raise an error if result < 0

        # Subtract and convert back into dollars and cents
        diff_cents = total_self - total_another  # Find the difference in cents
        dollars = diff_cents // 100  # Convert remaining cents to dollars
        cents = diff_cents % 100  # Find leftover cents
        return Money(dollars, cents)  # Return a new Money object with the result

# Test code
dc1 = Money(4, 5)
dc2 = Money(2, 95)

dc3 = dc1 + dc2
dc4 = dc1 - dc2
print(dc3)  # → 7.00 dollars
print(dc4)  # → 1.10 dollars
dc5 = dc2 - dc1  # should raise ValueError
