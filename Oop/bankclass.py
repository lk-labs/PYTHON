class bank:
    def __init__(self,bal):
        self.bal=bal
    def account_details(self):
        self.account=int(input("enter the account number:\n"))
        self.name=input("enter your name:\n")
    def deposit(self):
        self.depo=int(input("enter the amount to deposit:\n"))
        self.balance=self.depo+self.balance   
b=bank(0)
b.account_details()
b.deposit()
print("your account balance is",b.balance)
print(b.balance,b.name,b.account)