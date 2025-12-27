class CourseAttempt:
    def __init__(self, student_name, course_name,grade):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name} got grade {self.grade} from the course {self.course_name}"

def names_of_students(attempts: list):
    return list(map(lambda attempt: attempt.student_name, attempts))


s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

for name in names_of_students([s1, s2, s3]):
    print(name)


