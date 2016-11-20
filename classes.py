class BankAccount:
	def __init__(self):
		self.balance = 0
	def __init__(self, startingAmount):
		self.balance = startingAmount
	
	def getBalance(self):
		return self.balance
	
	def withdraw(self, withdrawAmount):
		self.balance -= withdrawAmount
		return self.balance
		
	def deposit(self, depositAmount):
		self.balance += depositAmount
		return self.balance
	
	def main(self)
		a = BankAccount()
		print a.getBalance()
		b = BankAccount(20)
		print b.getBalance()
		b.deposit(20)
		print b.getBalance()
		b.withdraw(30)
		print b.getBalance()
