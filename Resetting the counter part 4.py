class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.original_value = initial_value  # added for reset_original_value(self) to store the original value here

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value > 0:                  # this prevents the counter from going negative
            self.value = self.value - 1     # decrease the counter by 1

    #def set_to_zero(self):
    #    self.value = 0

    def reset_original_value(self):
        self.value = self.original_value

print()
counter = DecreasingCounter(55)               # create a counter starting at 55
counter.decrease()                            # decrease → value becomes 54
counter.decrease()                            # decrease → value becomes 53
counter.decrease()                            # decrease → value becomes 52
counter.decrease()                            # decrease → value becomes 51
counter.print_value()                         # prints "value: 51"
counter.reset_original_value()                # reset back to the starting value (55)
print("The original value is:", counter.original_value)
