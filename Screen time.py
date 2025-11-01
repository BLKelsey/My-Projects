# 1. Ask for the output filename
filename = input("Filename: ")

# 2. Ask for the starting date in month.day.year format
date_input = input("Starting date (month.day.year): ")

# 3. Split the input into numbers
parts = date_input.split(".")
start_month = int(parts[0])
start_day = int(parts[1])
start_year = int(parts[2])

# 4. Ask how many days we want to record
number_of_days = int(input("How many days: "))

# 5. Variables to track totals
total_minutes = 0
daily_data = []   # list to store entries for each day

# 6. Loop through each day
for i in range(number_of_days):
    current_day = start_day + i
    current_month = start_month   # month never changes (no rollover)
    current_year = start_year     # year never changes

    # ask for screen time data
    print(f"Screen time {current_month}.{current_day}.{current_year}:")
    tv_minutes = int(input("  TV minutes: "))
    computer_minutes = int(input("  Computer minutes: "))
    mobile_minutes = int(input("  Mobile minutes: "))

    # calculate total for this day
    daily_total = tv_minutes + computer_minutes + mobile_minutes

    # add to running total
    total_minutes += daily_total

    # store this day's record as text
    record = f"{current_month}.{current_day}.{current_year}: {tv_minutes}/{computer_minutes}/{mobile_minutes}"
    daily_data.append(record)

# 7. Calculate average screen time
average_minutes = total_minutes / number_of_days

# 8. Open the file for writing
with open(filename, "w") as f:
    # write summary
    f.write(f"Time period: {start_month}.{start_day}.{start_year}-"
            f"{start_month}.{start_day + number_of_days - 1}.{start_year}\n")
    f.write(f"Total minutes: {total_minutes}\n")
    f.write(f"Average minutes: {average_minutes:.2f}\n")

    # write each day's details
    for entry in daily_data:
        f.write(entry + "\n")

# 9. Let the user know it worked
print("Data stored in file", filename)
