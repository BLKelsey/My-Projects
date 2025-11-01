class LunchCard:                                  # Simple stored-value lunch card
    def __init__(self, balance: float):
        self.balance = balance                    # initial balance on the card

    def deposit_money(self, amount: float) -> None:
        if amount > 0:                            # accept only positive deposits
            self.balance += amount                # increase balance

    def subtract_from_balance(self, amount: float) -> bool:
        if self.balance >= amount:                # enough money to pay?
            self.balance -= amount                # deduct payment
            return True                           # payment succeeded
        return False                              # not enough funds

card = LunchCard(10.00)                              # create a card with $10
print()
print('Balance:', card.balance)                   # show starting balance
result = card.subtract_from_balance(8.00)            # try to pay $8
print('Payment Successful:', result)              # expect True
print()
print('Balance:', card.balance)                   # balance should now be $2
print('Try to spend 4.0')
result = card.subtract_from_balance(4.00)         # try to pay $4 (insufficient)
print('Payment Successful:', result, '(insufficient balance)')        # expect False
print('Balance:', card.balance)                   # still $2
