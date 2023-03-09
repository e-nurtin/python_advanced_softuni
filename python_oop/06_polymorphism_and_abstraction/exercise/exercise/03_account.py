class Account:
	def __init__(self, owner: str, starting_amount=0, transactions=list):
		self.owner = owner
		self.amount = starting_amount
		
		self._transactions = transactions
	
	def add_transaction(self, amount):
		if not isinstance(amount, int):
			raise ValueError("please use int for amount")
		self._transactions.append(amount)
	
	@property
	def balance(self):
		return self.amount + sum(self._transactions)
	
	@staticmethod
	def validate_transaction(account, amount):
		balance_after_transaction = account.balance() + amount
		
		if balance_after_transaction < 0:
			raise ValueError("sorry cannot go in debt!")
		
		account.add_transaction(amount)
		return f"New balance: {account.balance()}"
	
	def __str__(self):
		return f"Account of {self.owner} with starting amount: {self.amount}"
	
	def __repr__(self):
		return f"Account({self.owner}, {self.amount})"
	
	def __len__(self):
		return len(self._transactions)
	
	def __iter__(self):
		return self._transactions
	
	def __reversed__(self):
		return self._transactions
	
	def __ge__(self, other):
		return self.balance() >= other.balance()
	
	def __gt__(self, other):
		return self.balance() > other.balance()
	
	def __eq__(self, other):
		return self.balance() == other.balance()
	
	def __add__(self, other):
		account = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
		account._transactions = self._transactions + other._transactions
		return
	
	