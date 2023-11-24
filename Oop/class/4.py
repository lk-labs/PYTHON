"""
Deposit && create account
"""
class bank:
 def __int__(self,bal):
     self.balance=bal
 def account(self):
     self.name=str(input("Enter your name :"))
     self.accno=int(input("Enter account number :"))
 def deposit(self):
     self.depo=int(input("Enter ammount for deposit :"))
     self.balance=self.balance+self.depo

b=bank()

b.account()
b.deposit()
print("Your account balance is :" ,b.balance)
print(b.name,b.accno,b.balance)