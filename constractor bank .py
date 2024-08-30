class bank:
    def __init__(self,balance) :
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000
        
        
    def get_balance(self):
        return self.balance
        #print(f"Here is your get balance{self.balance}")
        
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            
    def withdraw(self,amount):
        if amount < self.min_withdraw :
            print(f"You can't withdraw below {self.min_withdraw}")
        elif amount > self.max_withdraw :
            print(f"You can't withdraw more than {self.max_withdraw}")
        else :
             self.balance -= amount
             print(f"Here is your balance  : {amount}")
             print(f"Here is your balance aFter withdraw : {self.balance}"   )

brac = bank(15000)
#brac.get_balance()
brac.deposit(10000)
brac.withdraw(5000)
brac.withdraw(500000)
brac.withdraw(50)

dbbl = bank(20000)
dbbl.get_balance()
dbbl.deposit(10000)
dbbl.withdraw(5000)
dbbl.withdraw(500000)
dbbl.withdraw(50)