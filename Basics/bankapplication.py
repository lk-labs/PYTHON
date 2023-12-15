class person:
    def __init__(self):
        self.balance=200
    def add_customer(self):
        self.customername=input("enter the customer name:")
        self.accountnumber=int(input("enter the account number:"))
        self.accountbranch=input("enter the branch of the account:")
class bank(person):
    def deposit(self):
        self.amount=int(input("enter the amount to be deposited:"))
        self.balance+= self.amount
    def withdrawal(self):
        self.drawal=int(input("enter the amount to withdraw:"))
        fee=36
        if self.drawal + fee <= self.balance:
            print("allowed to withdraw")
            self.balance-=self.drawal+fee
        elif self.balance< 200:
            print("not allowed to withdraw")
    def check_balance(self):
        print("balance",self.balance) 
    def exit_menu(self):
        print("exit menu")
b=bank() 
while True:
    print("**************************************")
    print("menu")
    print("1.register")
    print("2.deposit")
    print("3.withdraw")
    print("4.check balance")
    print("5.exit")

    choice=int(input("enter your choice:"))
    if choice== 1:
        b.add_customer()
    elif choice==2:
        b.deposit()
    elif choice==3:
        b.withdrawal()
    elif choice==4:
        b.check_balance()
    elif choice==5:
        b.exit_menu()    
    else:
        print("invalid choice")                
                         

                    