# Please write a program which asks the user for their date of birth, and then prints out how old the user was on the
# eve of the new millennium. The program should ask for the day, month and year separately, and print out the age in days.

import datetime                         # import the datetime module so we can work with dates

print()
day = int(input("Enter your day of birth: "))     # ask the user for the day and convert it to an integer
month = int(input("Enter your month of birth: ")) # ask the user for the month and convert it to an integer
year = int(input("Enter your year of birth: "))   # ask the user for the year and convert it to an integer

target_day = 31                        # set the target day (December 31)
target_month = 12                      # set the target month (December)
target_year = 1999                     # set the target year (1999)

# Convert the user's birth date into a date object (YYYY, MM, DD)
birth_date = datetime.date(year, month, day)

# Convert the target date into a date object (YYYY, MM, DD)
target_date = datetime.date(target_year, target_month, target_day)

# Calculate difference in days by subtracting two date objects
# .days extracts just the number of days from the timedelta result
age_in_days = (target_date - birth_date).days

if age_in_days < target_year:
    print("You weren't born yet on the eve of the new millennium.")
    exit()

print()
# Print out the result: how many days old the user was on 12/31/1999
print("On December 31, 1999, you were", age_in_days, "days old at the eve of the millennium..")










