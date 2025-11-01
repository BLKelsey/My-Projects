class SimpleDate:                                   # Define the SimpleDate class
    def __init__(self, month, day, year):           # Initialize with month, day, year
        self.month = month                          # Store the month
        self.day = day                              # Store the day
        self.year = year                            # Store the year

    def __str__(self):                              # Define how to print the date
        return f"{self.month}.{self.day}.{self.year}"  # Format: month.day.year

    def __add__(self, days):                        # Add operator: add days to a date
        new_day = self.day                          # Start with same day
        new_month = self.month                      # Start with same month
        new_year = self.year                        # Start with same year

        new_day += days                             # Add number of days

        # Adjust if day goes past number of days in current month
        while new_day > self.days_in_month(new_month, new_year):
            new_day -= self.days_in_month(new_month, new_year)   # Subtract month length
            new_month += 1                         # Move to next month

            if new_month > 12:                     # If month goes past December
                new_month = 1                      # Wrap to January
                new_year += 1                      # Increase the year

        return SimpleDate(new_month, new_day, new_year)  # Return new SimpleDate

    def days_in_month(self, month, year):           # Helper: number of days in month
        if month in [1, 3, 5, 7, 8, 10, 12]:        # Months with 31 days
            return 31
        elif month in [4, 6, 9, 11]:                # Months with 30 days
            return 30
        elif month == 2:                            # February
            if self.is_leap_year(year):             # Leap year check
                return 29
            else:
                return 28

    def is_leap_year(self, year):                   # Determine if year is leap year
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
                                                    # Leap years are divisible by 400, or 4 but not 100
# ---- Test section ----
d1 = SimpleDate(10, 4, 2020)                        # Create first date (Oct 4, 2020)
d2 = SimpleDate(12, 28, 1985)                       # Create second date (Dec 28, 1985)

d3 = d1 + 3                                         # Add 3 days → 10.7.2020
d4 = d2 + 400                                       # Add 400 days → 2.8.1987
print(d1)                                           # 10.4.2020
print(d2)                                           # 12.28.1985
print(d3)                                           # 10.7.2020
print(d4)                                           # 2.8.1987
