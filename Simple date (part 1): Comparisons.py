class SimpleDate:                                # Define a class representing a simple date
    def __init__(self, month, day, year):        # Constructor initializes the date parts
        self.month = month                           # Store the day value
        self.day = day                       # Store the month value
        self.year = year                         # Store the year value

    def __str__(self):                           # Controls how the object is printed
        return f"{self.month}.{self.day}.{self.year}"  # Format as day.month.year

    def __eq__(self, another):                   # Define '==' comparison
        # Return True if day, month, and year are all equal
        return (self.day == another.day and
                self.month == another.month and
                self.year == another.year)

    def __ne__(self, another):                   # Define '!=' comparison
        # Opposite of equality — True if not equal
        return not self.__eq__(another)

    def __lt__(self, another):                   # Define '<' comparison
        # Check year first
        if self.year < another.year:
            return True
        # If years are equal, compare months
        elif self.year == another.year and self.month < another.month:
            return True
        # If year and month are equal, compare days
        elif (self.year == another.year and
              self.month == another.month and
              self.day < another.day):
            return True
        else:
            return False                         # Otherwise, not less than

    def __gt__(self, another):                   # Define '>' comparison
        # Check year first
        if self.year > another.year:
            return True
        # If years are equal, compare months
        elif self.year == another.year and self.month > another.month:
            return True
        # If year and month are equal, compare days
        elif (self.year == another.year and
              self.month == another.month and
              self.day > another.day):
            return True
        else:
            return False                         # Otherwise, not greater than

# --- Test code ---
d1 = SimpleDate(10, 4, 2020)                     # Create first date object
d2 = SimpleDate(12, 28, 1985)                    # Create second date object
d3 = SimpleDate(12, 28, 1985)                    # Create third date object (same as d2)

print(d1)                                        # Display 4.10.2020
print(d2)                                        # Display 28.12.1985
print(d1 == d2)                                  # False — not the same
print(d1 != d2)                                  # True — they differ
print(d1 == d3)                                  # False — different year
print(d1 < d2)                                   # False — 2020 is later than 1985
print(d1 > d2)                                   # True — 2020 is later than 1985
