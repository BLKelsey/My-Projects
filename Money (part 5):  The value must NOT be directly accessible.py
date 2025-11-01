class Money:                                   # Define a class named Money
    def __init__(self, dollars, cents):        # Constructor
        self.__dollars = dollars
        self.__cents = cents

    def __str__(self):                         # How to display when printed
        return f"{self.__dollars}.{self.__cents:02d} dollars"

    def __add__(self, another):  # Defines behavior for the + operator
        # Convert both amounts into total cents to simplify math
        total_self = self.__dollars * 100 + self.__cents  # Convert this Money object to cents
        total_another = another.__dollars * 100 + another.__cents  # Convert the other Money object to cents

        # Add both totals together (in cents)
        total_cents = total_self + total_another

        # Convert total cents back into dollars and cents
        dollars = total_cents // 100  # Integer division gives whole dollars
        cents = total_cents % 100  # Modulo gives the remaining cents (0–99)

        # Return a new Money object with the sum (do not change existing objects)
        return Money(dollars, cents)

    def __sub__(self, another):  # Defines behavior for the - operator
        total_self = self.__dollars * 100 + self.__cents  # Convert this Money object to cents
        total_another = another.__dollars * 100 + another.__cents  # Convert the other Money object to cents

        # Check if subtraction would result in a negative amount
        if total_self < total_another:
            raise ValueError("Dollars cannot be negative")  # Stop and raise an error if result < 0

        # Subtract and convert back into dollars and cents
        diff_cents = total_self - total_another  # Find the difference in cents
        dollars = diff_cents // 100  # Convert remaining cents to dollars
        cents = diff_cents % 100  # Find leftover cents

        return Money(dollars, cents)  # Return a new Money object with the result

dc1 = Money(4, 5)
print(dc1)
dc1.dollars = 1000  # Does NOT modify the real value
print(dc1)




