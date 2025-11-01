class LotteryNumbers:
    def __init__(self, week: int, numbers: list):
        self.week = week                 # store the week number (for reference)
        self.numbers = numbers           # store the correct lottery numbers for that week

    def hits_in_place(self, numbers: list):
        return [num if num in self.numbers else -1    # keep num if it's found in the correct list; otherwise replace with -1
                for num in numbers]                   # loop through each number in the player's list

week8 = LotteryNumbers(8, [1, 2, 3, 10, 20, 30, 33])  # create an instance for week 8, with the correct winning numbers
my_numbers = [1, 4, 7, 10, 11, 20, 30]         # player's selected numbers for the same week
print()
print(week8.hits_in_place(my_numbers))         # print the resulting list where matches are kept and mismatches become -1
