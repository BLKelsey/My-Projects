# The exercise template contains a partially completed class DecreasingCounter:

class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        self.value = self.value -1   # Subtract 1 from value

counter = DecreasingCounter(10)
print()
counter.print_value()      # prints 10
counter.decrease()         # subtracts 1 → value becomes 9
counter.print_value()      # prints 9
counter.decrease()         # subtracts 1 → value becomes 8
counter.print_value()     # prints 8