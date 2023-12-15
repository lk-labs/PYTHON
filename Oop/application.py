class person:
    def __init__(self):
        self.bal=200
    def addcustomer(self):
        self.Cname=input("enter your customer name:")
        self.ACCNo=int(input("enter your account number:"))
        self.ACbranch=input("enter the name of branch:")
class bank(person):
    def deposit(self) :
        self.depo=int(input("enter amount to be deposited:"))
        self.bal=self.bal+self.depo
    def withdrawal(self):
        self.drawal=int(input("enter amount to withdraw:"))
        fee=36
        if self.bal >=self.drawal+fee:
            print("allowed to withdraw")
            self.bal=self.bal-self.drawal-fee
        elif self.bal<200:
              print("not allowed to withdraw")
              self.bal=self.bal 
    def customer_view(self):
        print(f"balnce is:{self.bal}")  
    def exit():
        print("exit") 
b=bank()            
while True:
    print("Bank application")
    print("Menu")
    print("1.register")
    print("2.deposit")
    print("3.withdrawal")
    print("4.check balance:")
    print("5.exit")
    choice=int(input("enter your choice:"))  

    if choice==1:
        b.addcustomer()
    elif choice==2:
        b.deposit()
    elif choice==3:
        b.withdrawal()
    elif choice==4:
        b.customer_view()
    elif choice==5:
        b.exit()                
    else:
        print("invalid choice")

