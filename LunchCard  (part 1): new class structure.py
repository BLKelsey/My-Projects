class LunchCard:
    def __init__(self,balance):
        self.balance = balance

    def to_string(self):
        return f"The balance is {self.balance:.1f} euros"

card = LunchCard(50)
print()
print(card.to_string())

