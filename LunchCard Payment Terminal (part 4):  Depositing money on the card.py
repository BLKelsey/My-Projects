class LunchCard:
    def __init__(self, balance: float):       # initialize LunchCard with starting balance
        self.balance = balance                # store balance as an attribute


class PaymentTerminal:
    price_lunch = 2.50                        # price of regular lunch
    price_special = 4.30                      # price of special lunch

    def __init__(self):
        self.funds = 1100.0                   # terminal starts with 1100.0 funds
        self.lunches = 0                      # counter for regular lunches sold
        self.specials = 0                     # counter for special lunches sold

    # ---- CASH payments ----
    def eat_lunch(self, payment: float) -> float:
        price = self.price_lunch
        if payment >= price:                  # if customer pays enough in cash
            self.funds += price               # add price to terminal funds
            self.lunches += 1                 # increase lunches sold count
            return payment - price            # return change
        return payment                        # not enough money → return full payment

    def eat_special(self, payment: float) -> float:
        price = self.price_special
        if payment >= price:                  # if customer pays enough in cash
            self.funds += price               # add price to terminal funds
            self.specials += 1                # increase specials sold count
            return payment - price            # return change
        return payment                        # not enough money → return full payment

    # ---- CARD payments ----
    def eat_lunch_lunchcard(self, card: LunchCard) -> bool:
        if card.balance >= self.price_lunch:  # if card has enough balance
            card.balance -= self.price_lunch  # deduct lunch price from card
            self.lunches += 1                 # increase lunches sold count
            return True                       # payment succeeded
        return False                          # not enough balance

    def eat_special_lunchcard(self, card: LunchCard) -> bool:
        if card.balance >= self.price_special:  # if card has enough balance
            card.balance -= self.price_special  # deduct special price from card
            self.specials += 1                  # increase specials sold count
            return True                         # payment succeeded
        return False                            # not enough balance

    def deposit_money_on_card(self, card, amount):
        if amount > 0:                         # only deposit positive amounts
            card.balance += amount             # add money to card balance
            # NOTE: funds at terminal do NOT increase here in your version


# ---- Main program ----
terminal = PaymentTerminal()                   # create terminal with 1100 funds
card = LunchCard(2)                            # create card with 2 balance

print(f"Card balance is {card.balance} dollars")

# Try to buy a special lunch (fails, only 2 dollars on card)
result = terminal.eat_special_lunchcard(card)  # attempt payment with card
print(f"Payment successful: {result}")         # False → not enough balance
print(f"Card balance is {card.balance} dollars")

# Deposit money onto card
terminal.deposit_money_on_card(card, 100)      # add 100 to card
print(f"Card balance is {card.balance} dollars")

# Try again to buy a special lunch (now succeeds)
result = terminal.eat_special_lunchcard(card)  # payment attempt
print(f"Payment successful: {result}")         # True → enough funds
print(f"Card balance is {card.balance} dollars")

# Print totals
print(f"Funds available at the terminal: {terminal.funds}")   # still 1100.0
print(f"Regular lunches sold: {terminal.lunches}")            # 0
print(f"Special lunches sold: {terminal.specials}")           # 1
