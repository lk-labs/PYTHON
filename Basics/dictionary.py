products={"code":"p001","name":"fridge","price":90000.00,"quantity":5,"expirydate":"30-10-2024"}
print(products)
print(len(products))

#accessing keys
print(products["price"])
#using the get method
print(products.get("code"))
#get the key values
print(products.keys())
#get the values 
print(products.values())
#get items in the list,it prints the keys and values

print(products.items())

#adding a new item
products["Reordervalue"]=3
print(products)

#updating 

products["price"]=120000.00
print(products)
#using the update inbuilt function
products.update({"quantity":10})
print(products)

#removing an item using pop(),removes specific item
products.pop("price")
print(products)

#removing the last item we use the popitem()

products.popitem()
print(products)

#using del method to remove a specific item
del products["quantity"]
print(products)