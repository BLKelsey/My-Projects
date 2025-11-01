# Write a function named list_years(dates: list) which takes a list of date type objects as its argument.
# The function should return a new list, which contains the years in the original list in chronological order, from earliest to latest.

from datetime import date

def list_years(dates: list):

    # 1. Create an empty list to hold the years
    years = []

    # 2. Go through each date in the list
    for date in dates:
        year = date.year    # take the year part of the date
        years.append(year)

    # 3. Sort the years list in order (earliest to latest)
    years.sort()

    # 4. Return the list of years
    return years

# Function call

date1 = date(2001, 2, 3)
date2 = date(2006, 10, 10)
date3 = date(1993, 5, 9)

years = list_years([date1, date2, date3])
print (years)