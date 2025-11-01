

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


stats = NumberStats()

print()
print("Please type in integer numbers (end with -1):")

while True:
    number = int(input("Type in an integer: "))
    if number == -1:
        break
    stats.add_number(number)

print()
print ("Sum of numbers:", stats.get_sum())
print ("Mean of numbers:", stats.average())


