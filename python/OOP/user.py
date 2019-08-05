class User:
    def __init__(self,username,email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_withdrawl(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print (self.name+"'s account balance: "+str(self.account_balance))
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount


brian = User("Brian Shmrian", "brian@brian.com")
bob = User("Bob Shmob", "bob@bob.com")
john = User("John Doe", "john@doe.com")

print ("Starting Brian's transactions")
brian.make_deposit(100)
brian.make_deposit(200)
brian.make_deposit(50)
brian.make_withdrawl(125)
brian.display_user_balance()

print("\nStarting Bob's transactions")
bob.make_deposit(120)
bob.make_deposit(35)
bob.make_withdrawl(25)
bob.make_withdrawl(12)
bob.display_user_balance()

print("\nStarting John's transactions")
john.make_deposit(350)
john.make_withdrawl(50)
john.make_withdrawl(50)
john.make_withdrawl(50)
john.display_user_balance()

print("\nTransferring from Brian to John")
brian.transfer_money(john,75)
brian.display_user_balance()
john.display_user_balance()


