class bank:
    def __init__(self):
        self.balance=0
    def accept(self):
        self.accountname=input("enter the account name:")
        self.employeeno=int(input("enter the employee number:"))
    def deposit(self):
        self.amount=int(input("enter the amount to be deposited:"))
        self.balance=self.balance+self.amount
    def withdrawal(self):
        self.drawal=int(input("enter the amount to be withdrawn:"))
        self.balance=self.balance-self.drawal
    def check_balance(self):
        print("balance",self.balance)


b=bank()
b.accept()
b.deposit()
b.withdrawal()
b.check_balance()        
