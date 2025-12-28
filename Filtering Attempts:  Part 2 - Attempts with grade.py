
class CourseAttempt:
    def __init__(self, student_name, course_name, grade):            # Constructor method (initializer)
        self.student_name = student_name                             # Stores the student's name
        self.course_name = course_name                               # Stores the course name
        self.grade = grade

    def __str__(self):  # Special method to define string representation of the object
        return f"{self.student_name} from the course {self.course_name} got grade {self.grade}"  # Returns a formatted, human-readable string

def attempts_with_grade(attempts: list, grade: int):                    # Defines a function that takes a list of CourseAttempt objects and a grade to match
    return filter(lambda attempt: attempt.grade == grade, attempts)     # Returns only those attempts whose grade is equal to the given grade

s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Introduction to AI", 3)
s4 = CourseAttempt("Olivia C. Objective", "Data Structures and Algorithms", 3)

for attempt in attempts_with_grade([s1, s2, s3, s4], 3):
    print(attempt)


