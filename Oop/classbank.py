class bank:
    def __init__(self,b):
        self.balance=b
    def checkbalance(self):
        print("your bank balance is",self.balance)   
#instantiate a class
amount=float(input("Enter amount to deposit:"))
b=bank(amount)
del b.balance
b.balance=25000
b.checkbalance()

