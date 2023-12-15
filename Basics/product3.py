class product:
    def __init__(self):
        self.productprice=0.00
    def add_new_product(self):
        self.productname=input("enter the name of product:")
        self.code=int(input("enter the code:"))
        self.description=input("enter the description of the product:")
class producttype(product):
    def add_new_product(self):
        super().add_new_product()
        self.productprice=int(input("enter the product price"))    
        self.category=input("enter the category of the product:")
    def search_product(self):
        self.mini_price=int(input("enter the minimum price of product:"))
        self.maxi_price=int(input("enter the maximum price:"))
        search_category=input("enter the category of the price:")
        if self.mini_price<=self.productprice<=self.maxi_price and search_category==self.category:
            print("name",self.productname)
            print("code",self.code)
            print("description",self.description)
            print("price",self.productprice)
        else:
            print("no matching criteria!")
    def exit_menu(self):
        print("exit")
p=producttype()
while True:
    print("********************************")
    print("menu") 
    print("1.addnewproduct")
    print("2.search_product")
    print("3.exit") 
    choice=int(input("enter your choice:"))
    if choice==1:
        p.add_new_product() 
    elif choice==2:
        p.search_product()
    elif choice==3:
        p.exit_menu()
    else:
        print("invalid choice")                             
