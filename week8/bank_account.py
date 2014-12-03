import random
import datetime
#class Database:

# a class is a function that produces an object
class Account(object):
	
	#class method to keep track of accounts 

    # init function 	
    def __init__(self,accountHolder,overDraftProtection):
        self.accountHolder = accountHolder
        self.balance = 0.00
        self.createdOn = '12-2-2014'
        self.overDraftProtection = overDraftProtection
    	
    def deposit(self,depositAmount):
        self.balance = self.balance + depositAmount
        return self.balance
    
    def getBalance(self):
		return self.balance # object has access to self.balance
		
    def withdraw(self,withDrawalAmount):
        if self.overDraftProtection: # then withdraw, whatever dude!
            self.balance = self.balance - withDrawalAmount
        elif withDrawalAmount <= self.balance:
            self.balance = self.balance - withDrawalAmount
        return self.balance
        
# THIS IS THE CONSTRUCTOR, SETS UP OBJECT 

# create some names for accounts
names = ['mark robinson','janet williams','will forte','bob purell','mary purell']

# create a dictionary whose keys are account numbers and whose
# values are account objects
bank_accounts = {}

#generating account keys here, which are strings
account_prefix = 'ID00'

# populate the dictionary with accounts
for index,name in enumerate(names):

    # make the full account id
    account_id = account_prefix + str(index)

    # set the account_id as the key to the newly created object
    bank_accounts[account_id] = Account(name,index%4)

	# deposit random amounts of money
    bank_accounts[account_id].deposit(random.randrange(400))

    # verify that the account was created
    print bank_accounts[account_id].getBalance()




