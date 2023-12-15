class Product:
    def __init__(self):
        self.price = 0.00

    def add_new_product(self):
        self.product_name = input("Enter the product name: ")
        self.product_code = int(input("Enter the product code: "))
        self.description = input("Enter the description of the product:")

class ProductType(Product):
    def add_new_product(self):
        super().add_new_product()
        self.price = int(input('Enter the price of the category: '))
        self.category = input("Enter the category of the product: ")

    def search_product(self):
        self.mini_price = int(input("Enter the minimum price of the product: ")) 
        self.maxi_price = int(input("Enter the maximum price of the product: "))
        search_category = input("Enter the product category to search:")

        if self.mini_price <= self.price <= self.maxi_price and search_category == self.category:
            print("\nDisplaying the product information:")
            print(f"Product Name: {self.product_name}")
            print(f"Description of Product: {self.description}")
            print(f"Product Code: {self.product_code}")
        else:
            print("\nNo matching criteria for the above search.")

    def exit_menu(self):
        print("Exiting the menu.")

p = ProductType()

while True:
    print("***********************************************")
    print("Product Catalogue")
    print("1. Add new product") 
    print("2. Search product")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        p.add_new_product()
        print("Product added successfully.")
    elif choice == 2:
        p.search_product()
    elif choice == 3:
        p.exit_menu()
        break
    else:
        print("Invalid choice! Please enter an integer between 1 and 3.")
