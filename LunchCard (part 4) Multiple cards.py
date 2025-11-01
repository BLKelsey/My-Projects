class LunchCard:
    def __init__(self,balance):
        self.balance = balance

    def __str__(self):   # Defines how the object is represented as a string (used by print and str())

        return f"The balance is {self.balance:.1f} euros"    # This method returns the balance as a formatted string with 1 decimal place

    def eat_lunch(self):
        self.balance -= 2.60      # Subtract the cost of a regular lunch (2.60 euros) from the balance

    def eat_special(self):
        self.balance -= 4.60     # Subtract the cost of a special lunch (4.60 euros) from the balance

    def deposit_money(self,amount):
        if amount < 0:
            raise ValueError ("You cannot deposit an amount of money less than zero")
        else:
            self.balance += amount

peters_card = LunchCard(20)
graces_card = LunchCard(30)

# Step 1
print()
peters_card.eat_special()
graces_card.eat_lunch()
print("Peter:", peters_card)
print("Grace:", graces_card)

# Step 2
peters_card.deposit_money(20)
graces_card.eat_special()
print("Peter:", peters_card)
print("Grace:", graces_card)

# Step 3
peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print("Peter:", peters_card)
print("Grace:", graces_card)





