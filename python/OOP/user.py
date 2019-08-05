class User:
    def __init__(self,username,email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print (self.name+"'s account balance: "+str(self.account_balance))
        return self
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
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


