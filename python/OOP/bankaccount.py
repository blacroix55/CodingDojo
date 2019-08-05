class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print ("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print ("Balance: "+str(self.balance))
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance*(1+self.int_rate)
        else:
            print ("Negative balance, not calculating interest")
        return self

brian=BankAccount(.06,100)
bob=BankAccount(.06)

brian.deposit(500).deposit(100).deposit(235).yield_interest().display_account_info()

bob.deposit(100).deposit(100).withdraw(250).withdraw(20).withdraw(20).withdraw(20).yield_interest().display_account_info()


