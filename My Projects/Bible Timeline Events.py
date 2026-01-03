# List of Bible events (just the names of the events)
event = [
    "Creation","The Fall", "The Flood", "Tower of Babel",
    "Call of Abraham", "Birth of Isaac","Birth of Jacob",
    "Israel's Slavery", "Exodus from Egypt", "Birth of Moses", "Burning Bush",
    "Ten Commandments", "Israel's First King", "David and Goliath",
    "David becomes King", "Solomon becomes King",
    "Solomon builds Temple", "Jesus is born",
    "Baptism of Jesus", "Temptation of Jesus",
    "Jesus Feeds the 5,000", "The Last Supper",
    "Crucifixion", "Jesus's Resurrection",
    "Pentecost", "Martyr of Stephen",
    "Saul's conversion", "John's Revelation"
]

# List of years that match each event above
# Negative numbers represent BC, positive numbers represent AD
year = [
    -4000, -4000, -2500, -2100,
    -2081, -2066, -2006,
    -1800, -1446, -1525, -1446,
    -1446, -1043, -1024,
    -1010, -967,
    -966, 5,
    26, 27,
    29, 28, 33,
    30, 30,
    30, 31,
    34, 95
]

# Bible references that explain where each event appears in Scripture
# These line up with the event and year lists by position
book = [
    "Genesis 1", "Genesis 3","Genesis 7", "Genesis 11",
    "Genesis 12", "Genesis 21", "Genesis 25",
    "Exodus 1", "Exodus 13-18", "Exodus 2", "Exodus 20",
    "Exodus 20", "1 Samuel 8-10", "1 Samuel 17",
    "2 Samuel 2", "2 Chronicles 1 & 1 Kings 3",
    "1 Kings 6", "Matthew 1, Mark 1, Luke 2:6, John 1:14",
    "Matthew 3:13, Mark 1:9, Luke 3:21", "Matthew 4, Mark 1:2, Luke 4",
    "Matthew 14:15, Mark 6:30, Luke 9, John 6",
    "Matthew 26:17–30, Mark 14:12–26, Luke 22:7–38, John 13",
    "Matthew 27, Mark 15, Luke 23, John 18 & 19",
    "Matthew 28, Mark 16, Luke 24, John 20 & 21",
    "Acts 2", "Acts 6 & 7",
    "Acts 9", "Revelation 1 - 22"
]

# ---------------- SORTING BY YEAR ----------------

timeline = []     # Create an empty list to hold the full timeline data

# Combine year, event, and book into one structure
# Each item becomes: (year, event, book)
for i in range(len(event)):                             #Repeat this loop once for each event, using i as the position number
    timeline.append((year[i], event[i], book[i]))       # [i] tells Python which position in the list to use so matching data stays together.

timeline.sort()       # Sort the timeline list by year because the year is the first value in each (year, event, book) tuple

# Show a numbered list of events so the user can choose one
print("\nBible Timeline Events:\n")

for index, item in enumerate(timeline, start=1):    # Loop through the timeline list and give each event a number starting at 1
                                                    # index = the event number shown to the user, item = one (year, event, book) entry
    print(index, "-", item[1])                      # item[1] is the event name

# Ask the user which event they want more details on
choice = input("\nWhich event would you like to pick? ")

# Check that the user entered a number
if choice.isdigit():
    choice = int(choice)

    # Make sure the number is within the valid range
    if 1 <= choice <= len(timeline):
        selected = timeline[choice - 1]  # Adjust because lists start at index 0

        # Display details for the chosen event
        print("\n== Biblical Event Details: ==")
        print()
        print("Event:", selected[1])
        print("Year:", selected[0])
        print("Book:", selected[2])
    else:
        print("Invalid number.")
else:
    print("Please enter a number.")
