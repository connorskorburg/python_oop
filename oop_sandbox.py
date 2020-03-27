class User:	
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)
    def make_deposit(self, amount):	
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(f"User: {self.name}")
        self.account.display_account_info()
        return self
    def transfer_money(self, amount, User):
        self.account.withdraw(amount)
        User.account.deposit(amount)
        self.account.display_account_info()
        User.account.display_account_info()
        return self
class BankAccount:
    def __init__(self, int_rate = 0.02, balance = 0):
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
        if self.balance > 0:
            self.balance = int(self.int_rate * self.balance) + self.balance
            return self
        else:
            return self
account_owner1 = User("Bob", "bob@mail.com").make_deposit(500).make_deposit(200).make_deposit(1000).make_withdrawal(500).display_user_balance()

# Bob = User("Bob", "bob@mail.com").account.deposit(100).deposit(200).deposit(500).withdraw(300).yield_interest().display_account_info()
# Bob.account = BankAccount(0.05, 500)
# Bob.account.display_account_info()
# Balance: $1050

