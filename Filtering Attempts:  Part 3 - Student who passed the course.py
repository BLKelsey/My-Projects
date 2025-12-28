class CourseAttempt:
    def __init__(self, student_name, course_name, grade):            # Constructor method (initializer)
        self.student_name = student_name                             # Stores the student's name
        self.course_name = course_name                               # Stores the course name
        self.grade = grade

    def __str__(self):  # Special method to define string representation of the object
        return f"{self.student_name}"

def passed_students(attempts: list, course: str):
    return sorted(map(lambda attempt: attempt.student_name,       # Extracts student names (map) from attempts and returns them as an alphabetically sorted list
           filter(lambda attempt: attempt.course_name == course and attempt.grade > 0, attempts)))  # Keeps only CourseAttempt objects for the given course with a passing grade (> 0)


s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)

for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
    print(attempt)