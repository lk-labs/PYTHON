class product:
    def __init__(self):
        self.price=0.00
    def add_newproduct(self):
        self.productname=input("enter the product name:")
        self.productcode=int(input("enter the product code:"))
        self.description=input("enter the descripton of the product:")
class product_type(product):
    def add_newproduct(self):
        super().add_newproduct()
        self.price=int(input('enter the price of the category'))
        self.category=input("enter the category of the procuct:")
        
    def search_product(self):
        self.miniprice=int(input("enter the miniprice of the product:")) 
        self.maxiprice=int(input("enter the maxi price of the product:"))
        search_category=input("enter the product category:")

        if  self.miniprice<=self.price<=self.maxiprice and search_category==self.category:
            print("display the product information")
            print(f"the product name:{self.productname}")
            print(f"description of product:{self.description}")
            print(f"product code :{self.productcode}")
        else:
            print("no matching criteria for the above search")
    def exit(self):
        print("exit menu")
p=product_type()
while True:
    print("***********************************************")
    print("product catalogue")
    print("1.add new product") 
    print("2.search product")
    print("3.exit")

    choice=int(input("enter your choice"))
    if choice==1:
        p.add_newproduct()
        print("product added successfully")
    elif choice==2:
        p.search_product()
    elif choice==3:
        p.exit()
        break
    else:
        print("invalid choice!pleaase enter an interger between 1 and 3")                    
            