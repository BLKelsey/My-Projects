import urllib.request
import json

def retrieve_all():

    # 1. Retrieve the data from the internet
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read()
    data = data.decode("utf-8")      # Convert bytes → string
    data = json.loads(data)          # Convert string → Python object (list/dict)

    # 2. Prepare a list to store active courses
    courses = []

    # 3. Go through each course in the JSON data
    for course in data:
        if course["enabled"] is True:   # only active courses
            course_name = course["fullName"]
            short_name = course["name"]
            year = course["year"]
            total_exercises = sum(course["exercises"])     # Sum all course exercises
            courses.append((course_name, short_name, year, total_exercises))   # Add this course as a tuple into the list

    # 4. Return all active courses
    return courses

# Function call
all_courses = retrieve_all()
print("[")                                # Print the opening square bracket of the list
for course in all_courses:                # Go through each course in the list of all_courses
    print("    " + str(course) + ",")     # Print the course as a string, indented with 4 spaces, followed by a comma
print("]")                                # Print the opening square bracket of the list

