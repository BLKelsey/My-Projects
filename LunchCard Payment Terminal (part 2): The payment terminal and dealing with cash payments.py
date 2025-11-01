class PaymentTerminal:                                  # Handles cash payments for lunches
    def __init__(self):
        self.funds = 1000                               # starting cash in the terminal
        self.lunches = 0                                # count of regular lunches sold
        self.specials = 0                               # count of special lunches sold
        self.price_lunch = 2.50                         # price of a regular lunch
        self.price_specials = 4.30                      # price of a special lunch

    def eat_lunch(self, payment: float):                # customer pays for a regular lunch with cash
        price = self.price_lunch                        # regular lunch price
        if payment >= price:                            # enough cash?
            self.funds = self.funds + price             # terminal keeps the price amount
            self.lunches = self.lunches + 1             # record one lunch sold
            change = payment - price                    # compute change
            return change                               # give back the change
        else:
            return payment                              # not enough: sale fails, return all cash

    def eat_special(self, payment: float):              # customer pays for a special lunch with cash
        price = self.price_specials                     # special lunch price
        if payment >= price:                            # enough cash?
            self.funds = self.funds + price             # add price to terminal funds
            self.specials = self.specials + 1           # record one special sold
            change = payment - price                    # compute change
            return change                               # return change
        else:
            return payment                              # not enough: refund full amount

terminal = PaymentTerminal()                            # create a terminal instance
print()

change = terminal.eat_lunch(10.0)                       # pay $10 for $2.50 lunch → change 7.50
print("Paid $10 for $2.50 lunch. The change returned: ", change)

change = terminal.eat_lunch(5.0)                        # pay $5 for $2.50 lunch → change 2.50
print("Paid $5 for $2.50 lunch. The change returned: ", change)

change = terminal.eat_special(4.30)                     # exact payment for special → change 0.00
print("Exact payment for special lunch. The change returned: ", change)
print()

print("Funds available at the terminal:", terminal.funds)   # total cash now in terminal
print("Regular lunches sold:", terminal.lunches)             # how many regular lunches sold
print("Special lunches sold:", terminal.specials)            # how many specials sold
