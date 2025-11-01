class ExamResult:  # Define a class to store a student's name and three grades
    def __init__(self, names, grade1, grade2, grade3):  # Initialize attributes when an object is created
        self.names = names
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

def best_results(results: list): return [max(result.grade1, result.grade2, result.grade3) for result in results]  # Return a list of the highest grade for each student

result1 = ExamResult("Peter", 5, 3, 4)  # Create first ExamResult object
result2 = ExamResult("Pippa", 3, 4, 1)  # Create second ExamResult object
result3 = ExamResult("Paul", 2, 1, 3)   # Create third ExamResult object
results = [result1, result2, result3]   # Put all ExamResult objects into a list
print()  # Print a blank line for spacing
print("The highest grade from each student:", (best_results(results)))  # Print the best (highest) grade from each ExamResult
