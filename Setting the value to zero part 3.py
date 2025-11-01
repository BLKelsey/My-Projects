# Add a method set_to_zero which sets the value of the counter to 0

class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    #def decrease(self):
    #    if self.value > 0:                  # this prevents the counter from going negative
    #        self.value = self.value - 1     # decrease the counter by 1

    def set_to_zero(self):
        self.value = 0

print()
counter = DecreasingCounter(100)   # create a new counter object starting with value 100
counter.print_value()              # print the current value (expected: 100)
counter.set_to_zero()              # call the method, which sets the counter’s value to 0
counter.print_value()              # print the updated value (expected: 0)
