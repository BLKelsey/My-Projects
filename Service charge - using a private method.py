class BankAccount:
    def __init__(self, name: str, acct_num: str, balance: float):   # Constructor: set up account
        self.__name = name                                          # Private attribute for account holder's name
        self.__acct_num = acct_num                                  # Private attribute for account number
        self.__balance = balance                                    # Private attribute for balance

    def deposit(self, amount: float):                               # Public method: deposit money
        self.__balance += amount                                    # Increase balance by amount
        self.__service_charge()                                     # Apply 1% service charge

    def withdraw(self, amount: float):                              # Public method: withdraw money
        self.__balance -= amount                                    # Decrease balance by amount
        self.__service_charge()                                     # Apply 1% service charge

    @property
    def balance(self):                                              # Property: returns current balance
        return self.__balance

    def __service_charge(self):                                     # Private helper method
        fee = self.__balance * 0.01                                 # Calculate 1% of current balance
        self.__balance -= fee                                       # Subtract fee from balance

# --- Main Programe ---
account = BankAccount("Randy Riches", "12345-6789", 1000)     # Create account with $1000

account.withdraw(100)                                               # Withdraw 100 → balance 900 → fee 9 → 891
print()
print(account.balance)                                              # Prints 891.0

account.deposit(100)                                                # Deposit 100 → balance 991 → fee 9.91 → 981.09
print(account.balance)                                              # Prints 981.09
