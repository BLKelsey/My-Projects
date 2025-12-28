class CourseAttempt:
    def __init__(self, student_name, course_name, grade):            # Constructor method (initializer)
        self.student_name = student_name                             # Stores the student's name
        self.course_name = course_name                               # Stores the course name
        self.grade = grade                                           # Stores the grade

    def __str__(self):                                               # Special method to define string representation of the object
        return f"{self.student_name} got grade {self.grade} from the course {self.course_name}"  # Returns a formatted, human-readable string

def course_names(attempts: list):                                                    # Function that takes a list of CourseAttempt objects
    return sorted(set(map(lambda attempt: attempt.course_name, attempts)))           # Extracts course names → removes duplicates (set) → sorts (sorted) → returns list

# ----Main program----
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)                # Creates first CourseAttempt instance
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)         # Creates second CourseAttempt instance (same course)
s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)             # Creates third CourseAttempt instance (different course)

for name in course_names([s1, s2, s3]):                                              # Calls the function (course_names) with the list of attempts and iterates over result
    print(name)                                                                      # Prints each unique course name (sorted alphabetically)