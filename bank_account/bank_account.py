class BankAccount:
    def __init__(self, int_rate = 0.0, balance = 0):
        self.balance = balance
        self.int_rate = int_rate
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
            self.balance -= amount
            return self
        else:
            self.balance -= amount
            return self
    def display_account_info(self):
        if self.balance > 0:
            print(f"Balance: ${self.balance}")
        elif self.balance < 0:
            self.balance *= -1
            print(f"Balance: -${self.balance}")
            return self
        else:
            return self
        return self
    def yield_interest(self):
        if self.balance >= 0:
            self.balance = int(self.int_rate * self.balance) + self.balance
            return self
        else:
            return self

Account1 = BankAccount(0.05, 500).deposit(100).deposit(200).deposit(500).withdraw(300).yield_interest().display_account_info()
# Balance: $1050
Account2 = BankAccount(0.01, 1000).deposit(250).deposit(250).withdraw(500).withdraw(300).withdraw(200).withdraw(1000).yield_interest().display_account_info()
# Balance: -$505