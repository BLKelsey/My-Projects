class ExamSubmissions:
    def __init__(self, examinee: str, points: int):
        self.examinee = examinee
        self.points = points


# Takes a list of ExamSubmissions and an integer (lowest_passing) as arguments
def passed(submissions: list[ExamSubmissions], lowest_passing: int):
    result = []   # create an empty list to store submissions that pass
    for submission in submissions:   # go through each submission in the list
        if submission.points >= lowest_passing:   # check if the points are enough to pass
            result.append(submission)   # add the submission to the result list
    return result   # return the list of passing submissions

if __name__ == "__main__":
    # Create several ExamSubmissions objects with examinee name and points
    s1 = ExamSubmissions("Peter", 12)
    s2 = ExamSubmissions("Pippa", 19)
    s3 = ExamSubmissions("Paul", 15)
    s4 = ExamSubmissions("Phoebe", 9)
    s5 = ExamSubmissions("Persephone", 17)

# Call the passed() function with all submissions, requiring at least 15 points to pass
kept = passed([s1, s2, s3, s4, s5], 15)

# Loop through the passing submissions
print()
for each in kept:
    # Print the name and points of each passing submission
    print("ExamSubmissions (examinee:", each.examinee, ", points:", each.points, ")")





