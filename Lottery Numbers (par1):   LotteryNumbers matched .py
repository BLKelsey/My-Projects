class LotteryNumbers:
    def __init__(self, week: int, correct_numbers: list):
        self.week = week                       # store the week number
        self.correct_numbers = correct_numbers  # store the correct lottery numbers

    def number_of_hits(self, numbers: list):
        return len([num for num in numbers if num in self.correct_numbers])
        # create a list of all numbers that exist in both 'numbers' and 'self.correct_numbers'
        # count how many matches there are using len()

week5 = LotteryNumbers(5, [1, 2, 3, 4, 5, 6, 7])
my_numbers = [1, 4, 7, 11, 13, 19, 24]
print(week5.number_of_hits(my_numbers))
