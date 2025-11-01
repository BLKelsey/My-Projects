class NumberStats:
    def __init__(self):
        self.count = 0
        self.total_sum = 0

    def add_number(self, value):
        self.total_sum += value
        self.count += 1

    def get_sum(self):
        return self.total_sum

    def get_count(self):
        return self.count

    def average(self):
        if self.count == 0:
            return 0
        else:
            return self.total_sum / self.count

# --- Main Program ---
stats_all = NumberStats()
stats_even = NumberStats()
stats_odd = NumberStats()

print("Please type in integer numbers (end with -1):")

while True:
    user_input = int(input("Type in an integer: "))
    if user_input == -1:
        break

    stats_all.add_number(user_input)   # track all numbers

    if user_input % 2 == 0:            # track evens
        stats_even.add_number(user_input)
    else:                              # track odds
        stats_odd.add_number(user_input)

print()
print("Sum of numbers:", stats_all.get_sum())
print("Mean of numbers:", stats_all.average())
print("Sum of even numbers:", stats_even.get_sum())
print("Sum of odd numbers:", stats_odd.get_sum())
print()
print("Count of even numbers:", stats_even.get_count())
print("Count of odd numbers:", stats_odd.get_count())

