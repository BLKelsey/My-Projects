class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance


class PaymentTerminal:
    price_lunch = 2.50
    price_special = 4.30

    def __init__(self):
        self.funds = 1000.0
        self.lunches = 0
        self.specials = 0

    # ---- CASH payments ----
    def eat_lunch(self, payment: float) -> float:
        price = self.price_lunch
        if payment >= price:
            self.funds += price
            self.lunches += 1
            return payment - price
        return payment

    def eat_special(self, payment: float) -> float:
        price = self.price_special
        if payment >= price:
            self.funds += price
            self.specials += 1
            return payment - price
        return payment

    # ---- CARD payments ----
    def eat_lunch_lunchcard(self, card: LunchCard) -> bool:
        if card.balance >= self.price_lunch:
            card.balance -= self.price_lunch
            self.lunches += 1
            return True
        return False

    def eat_special_lunchcard(self, card: LunchCard) -> bool:
        if card.balance >= self.price_special:
            card.balance -= self.price_special
            self.specials += 1
            return True
        return False

# Main program
terminal = PaymentTerminal()

change = terminal.eat_lunch(10.0)            # costs 2.50.  change 7.5, funds +2.5
print()
print("The change returned was", change)

card = LunchCard(7)

print("Payment successful:", terminal.eat_special_lunchcard(card))  # True (card = 2.7)
print("Payment successful:", terminal.eat_special_lunchcard(card))  # False
print("Payment successful:", terminal.eat_lunch_lunchcard(card))    # True (card = 0.2)
print()
print("Funds available at the terminal:", terminal.funds)  # 1002.5
print("Regular lunches sold:", terminal.lunches)           # 2 (1 cash + 1 card)
print("Special lunches sold:", terminal.specials)          # 1
