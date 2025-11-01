# Add functionality to your decrease method, so that the value of the counter will never reach negative values.
# If the value of the counter is 0, it will not be further decreased. For example, 2, 1, 0, 0


class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value > 0:                  # this prevents the counter from going negative
            self.value = self.value - 1     # decrease the counter by 1


counter = DecreasingCounter(2)
print()
counter.print_value()      # prints 2
counter.decrease()         # subtracts 1 → value becomes 1
counter.print_value()      # prints 1
counter.decrease()         # subtracts 1 → value becomes 0
counter.print_value()      # prints 0
counter.decrease()         # subtracts 0 -> value should still be 0 (no negative nums allowed)
counter.print_value()      # prints 0