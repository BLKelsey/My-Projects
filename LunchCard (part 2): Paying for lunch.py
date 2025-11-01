class LunchCard:
    def __init__(self,balance):
        self.balance = balance

    def to_string(self):
        return f"The balance is {self.balance:.1f} euros"    # This method returns the balance as a formatted string with 1 decimal place

    def eat_lunch(self):
        self.balance -= 2.60      # Subtract the cost of a regular lunch (2.60 euros) from the balance

    def eat_special(self):
        self.balance -= 4.60     # Subtract the cost of a special lunch (4.60 euros) from the balance

card = LunchCard(50)           # create a new LunchCard with an initial balance of 50 euros
print()                        # just prints an empty line for spacing
print(card.to_string())        # print the current balance (50.0 euros)
card.eat_lunch()               # pay for one lunch → balance decreases by 2.60
print(card.to_string())        # print the updated balance
card.eat_special()             # pay for one special lunch → balance decreases by 4.60
card.eat_lunch()               # pay for another regular lunch → balance decreases by 2.60
print(card.to_string())        # print the updated balance again


