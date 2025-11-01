import urllib.request
import json

def retrieve_course(course_name: str):
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses/" + course_name + "/stats"
    response = urllib.request.urlopen(url)
    data = response.read()
    stats = json.loads(data)

    total_weeks = len(stats)
    total_students = 0
    total_hours = 0
    total_exercises = 0

    for week in stats.values():
        total_students += week["students"]
        total_hours += week["hour_total"]
        total_exercises += week["exercise_total"]

    hours_average = total_hours // total_students
    exercises_average = total_exercises // total_students

    result = {
        "weeks": total_weeks,
        "students": total_students,
        "hours": total_hours,
        "hours_average": hours_average,
        "exercises": total_exercises,
        "exercises_average": exercises_average
    }

    return result


# Example usage with pretty formatting
course_stats = retrieve_course("docker2019")

# Use json.dumps to format dictionary with new lines and indents
print(json.dumps(course_stats, indent=4))
