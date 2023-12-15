class person:
    def Addcustomer(self):
        self.customername=input("enter the customername:")
        self.accountnumber=int(input("enter the account number:"))
        self.branc_account=input("enter the branch of the account:")
class bank(person):
    def __init__(self):
        self.bal=200
    def deposit(self):
        self.depo=int(input("enter the amount to be deposited:"))
        self.bal=self.bal+self.depo
    def withdrawal(self):
        self.drawal=int(input("enter the amount to withdrawal"))
        if self.bal>=200:
            print("allowed to withdraw")
            fee=36
            self.bal=self.bal-self.drawal-fee
        elif self.bal <200:
            print("not allowed to withdraw")    
    def check_balance(self):
        print("the bank balance is",self.bal) 
    def exit(self):
        print("exit") 

b=bank()
while True:
    print("Menu:")
    print("1. Register Customer")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Check Balance")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        b.Addcustomer()
    elif choice == 2:
        b.deposit()
    elif choice == 3:
        b.withdrawal()
    elif choice == 4: 
        b.check_balance()
    elif choice == 5:
        b.exit()
        break
    else:
        print("Invalid choice. Please try again.")          

        