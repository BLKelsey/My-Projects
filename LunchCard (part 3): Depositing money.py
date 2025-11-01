class LunchCard:
    def __init__(self,balance):
        self.balance = balance

    def to_string(self):
        return f"The balance is {self.balance:.1f} euros"    # This method returns the balance as a formatted string with 1 decimal place

    def deposit_money(self,amount):
        if amount < 0:
            raise ValueError ("You cannot deposit an amount of money less than zero")
        else:
            self.balance += amount

card = LunchCard(10)
print()
print(card.to_string())
card.deposit_money(-10)
print(card.to_string())







