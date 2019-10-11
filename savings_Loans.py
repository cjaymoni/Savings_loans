import random

class User_Account: 
	def __init__(self): 
		self.balance = 0
		self.name = "Unknown"
		self.acc_Number = 0
		print("Hello!!! Welcome to Action Savings and Loans")

	def register(self): 
		user_name = input("Enter Your Name: ") 
		self.name = user_name  
		self.acc_Number = random.randint(10000000,99999999)
		print("Will you like to deposit an initial amount?")
		ans = input("(yes | no): ")
		if (ans == 'yes'):
			self.deposit()
			self.display()
			start()
		else:
			self.display()
			start()
		

	def deposit(self): 
		amount=float(input("Enter amount to be Deposited: ")) 
		self.balance += amount 
		print("\nAmount Deposited:",amount) 
		self.display()
		start()

	def withdraw(self): 
		amount = float(input("Enter amount to be Withdrawn: ")) 
		if self.balance>=amount: 
			self.balance-=amount 
			print("\nYou Withdrew:", amount) 
			self.display()
			start()
		else: 
			print("\nInsufficient funds ")
			self.display()
			start()

	def display(self): 
		print("\n*********************************************")
		print("* Customer's Name",self.name) 
		print("* Account Number",self.acc_Number) 
		print("* Net Available Balance =",self.balance)
		print("*********************************************")
		start()


# creating an object of class 
s = User_Account() 

def start():
	print("\n Choose from the options below: \n\t 1.Create Account \n\t 2.Deposit \n\t 3.Withdraw \n\t 4.Check Balance")
	option = int(input("Response: "))
	if (option == 1):
		s.register()

	elif (option == 2):
		s.deposit()

	elif (option == 3):
		s.withdraw()

	elif (option == 4):
		s.display()

	else:
		print("Invalid Input")
		start()

start()