# The function should return a new list of CourseAttempt objects, including only those items from the original list whose grade is at least 1.

class CourseAttempt:
    def __init__(self, student_name, course_name, grade):            # Constructor method (initializer)
        self.student_name = student_name                             # Stores the student's name
        self.course_name = course_name                               # Stores the course name
        self.grade = grade

    def __str__(self):  # Special method to define string representation of the object
        return f"{self.student_name} from the course {self.course_name} got grade {self.grade}"  # Returns a formatted, human-readable string

def accepted(attempts: list):
    return list(filter(lambda attempt: attempt.grade >= 1, attempts))   # lambda creates an anonymous function that returns a new list
                                                                        # containing only CourseAttempt objects whose grade is at least 1


s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 0)

for attempt in accepted([s1, s2, s3]):   # Loops through only the CourseAttempt objects (from lambda anonymous function) that have a grade of 1 or higher
    print(attempt)
