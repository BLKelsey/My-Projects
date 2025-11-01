
class NumberStats:
    def __init__(self):
        self.count = 0   # keep track of how many numbers were added
        self.total_sum = 0

    def add_number(self,number):
        self.count += 1  # increase count by 1 each time add_number is called
        self.total_sum += number

    def count_numbers(self):
        return self.count  # return how many numbers have been added

    def get_sum(self):
        return self.total_sum

    def average(self):
        if self.count == 0:
            return 0
        else:
            return self.total_sum / self.count

print()
stats = NumberStats()
stats.add_number(3)
stats.add_number(5)
stats.add_number(1)
stats.add_number(2)

print("Numbers added:", stats.count_numbers())   # → 4
print ("Sum of numbers:", stats.get_sum())        # → 11
print ("Mean of numbers:", stats.average())      # → 2.75

