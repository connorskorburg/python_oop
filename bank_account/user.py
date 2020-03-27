class User:	
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.account_balance = 0
	def make_deposit(self, amount):	
		self.account_balance += amount
	def make_withdrawal(self, amount):
		self.account_balance -= amount
	def display_user_balance(self):
		print(f"User: {self.name}, Balance: ${self.account_balance}")
	def transfer_money(self, amount, User):
		self.account_balance -= amount
		User.account_balance += amount
		self.display_user_balance()
		User.display_user_balance()

Bob = User("Bob", "bob@mail.com")
Bob.make_deposit(500)
Bob.make_deposit(200)
Bob.make_deposit(1000)
Bob.make_withdrawal(500)
Bob.display_user_balance()

John = User("John", "john@mail.com")
John.make_deposit(1000)
John.make_deposit(300)
John.make_withdrawal(200)
John.make_withdrawal(500)
John.display_user_balance()

Connor = User('Connor', 'connor@mail.com')
Connor.make_deposit(5000)
Connor.make_withdrawal(500)
Connor.make_withdrawal(1000)
Connor.make_withdrawal(300)
Connor.display_user_balance()

Bob.transfer_money(200, Connor)

# User: Bob, Balance: $1200
# User: John, Balance: $600
# User: Connor, Balance: $3200
# User: Bob, Balance: $1000
# User: Connor, Balance: $3400