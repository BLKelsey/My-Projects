
class NumberStats:
    def __init__(self):
        self.count = 0   # keep track of how many numbers were added

    def add_number(self,number):
        self.count += 1  # increase count by 1 each time add_number is called

    def count_numbers(self):
        return self.count  # return how many numbers have been added


# Example usage
print()
stats = NumberStats()
stats.add_number(3)
stats.add_number(5)
stats.add_number(1)
stats.add_number(2)

print("Numbers added:", stats.count_numbers())

