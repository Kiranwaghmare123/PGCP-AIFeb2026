class BankAccount:
    bank = "SBI"
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    
    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)
    
    
    def withdraw(self, amount):
        self.balance -= amount
        print("Amount Withdraw:", amount)
    
    def showbal(self):
        print(self.name, " ",self.balance)
        
a1 = BankAccount("Shyam", 50000)
a2 = BankAccount("Priya", 10000)
    
a1.deposit(2000)
a1.showbal()
a1.withdraw(1000)
a1.showbal()