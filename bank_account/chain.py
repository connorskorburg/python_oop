class User:	
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.account_balance = 0
	def make_deposit(self, amount):	
		self.account_balance += amount
		return self
	def make_withdrawal(self, amount):
		self.account_balance -= amount
		return self
	def display_user_balance(self):
		print(f"User: {self.name}, Balance: ${self.account_balance}")
		return self
	def transfer_money(self, amount, User):
		self.account_balance -= amount
		User.account_balance += amount
		self.display_user_balance()
		User.display_user_balance()
		return self

Bob = User("Bob", "bob@mail.com").make_deposit(500).make_deposit(200).make_deposit(1000).make_withdrawal(500).display_user_balance()

John = User("John", "john@mail.com").make_deposit(1000).make_deposit(300).make_withdrawal(200).make_withdrawal(500).display_user_balance()

Connor = User('Connor', 'connor@mail.com').make_deposit(5000).make_withdrawal(500).make_withdrawal(1000).make_withdrawal(300).display_user_balance()

Bob.transfer_money(200, Connor)

# User: Bob, Balance: $1200
# User: John, Balance: $600
# User: Connor, Balance: $3200
# User: Bob, Balance: $1000
# User: Connor, Balance: $3400