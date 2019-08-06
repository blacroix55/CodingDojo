class User:
    def __init__(self,username,email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.deposit(amount) # the specific user's account increases by the amount of the value received
        return self
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print (self.name+"'s account balance: "+str(self.account.balance))
        return self
    def transfer_money(self,other_user,amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self

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
        print ("Balance: "+str(self.balance) )
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance*(1+self.int_rate)
        else:
            print ("Negative balance, not calculating interest")
        return self

brian = User("Brian Shmrian", "brian@brian.com")
bob = User("Bob Shmob", "bob@bob.com")
john = User("John Doe", "john@doe.com")

print ("Starting Brian's transactions")
brian.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawl(125).display_user_balance()

print("\nStarting Bob's transactions")
bob.make_deposit(120).make_deposit(35).make_withdrawl(25).make_withdrawl(12).display_user_balance()

print("\nStarting John's transactions")
john.make_deposit(350).make_withdrawl(50).make_withdrawl(50).make_withdrawl(50).display_user_balance()

print("\nTransferring from Brian to John")
brian.transfer_money(john,75).display_user_balance()
john.display_user_balance()

