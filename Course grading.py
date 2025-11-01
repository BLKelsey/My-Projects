# Please write a program which asks the user for the names of these two files, reads the files,
# and then prints out the total number of exercises completed by each student.


names = {}   # create an empty dictionary to store student id → full name

# Step 1: Read student names
with open("Students.csv", encoding="utf-8-sig") as new_file:
    for line in new_file:                    # read each line in the file
        line = line.strip()                  # remove whitespace and newline
        parts = line.split(";")              # split the line into columns

        if parts[0].strip().lower() == "id": # skip the header row
            continue

        student_id = parts[0]                # first column = student id
        full_name = f"{parts[1]} {parts[3]}" # combine first name (col 2) + last name (col 4)
        names[student_id] = full_name        # store in dictionary: id → "first last"


# Step 2: Read exercise totals into dictionary: total score for exercises
scores = {}  # dictionary for student id → total exercises completed

with open("Exercises.csv", encoding="utf-8-sig") as new_file:
    for line in new_file:
        line = line.strip()                 # remove whitespace and newline
        parts = line.split(";")             # split the line into columns

        if parts[0].strip().lower() == "id": # skip the header row
            continue

        student_id = parts[0]               # first column = student id

        total = 0                           # running sum of exercise scores
        for string in parts[1:]:            # loop through exercise columns
            if string:                      # skip empty values
                total += int(string)        # convert to int and add to total

        scores[student_id] = total          # store id → total score in dictionary


# Step 3: Print results
print()
print("Student information: Students.csv")
print("Exercises completed: Exercises.csv")

for student_id in names:                    # go through all student ids from names
    if student_id in scores:                # only print if that id has exercise data
        print(names[student_id], scores[student_id])  # print full name + total
