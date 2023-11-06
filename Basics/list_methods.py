#to check present of an item in a list we use in if and in

cars=["volvo","passat","benz","Audi"]
#cars.insert(1,"ferrali")
print(cars)
#adding an item at the end
#cars.append("toyota")
print(cars)
#using extend method
#cars_2=["vitz","Demio"]
#cars.extend(cars_2)
print(cars)
#removing an item in a list we use remove and pop (uses index) together with del
#cars.remove("benz")
print(cars)
#using pop
#cars.pop(0)
print(cars)
#using the pop to remove the last item
cars.pop()
print(cars)
#using del keyword []
#del cars 
#print(cars)
#clearing a list
#cars.clear()
#print(cars)

val=input("enter item to search for:\n")
if val in cars:
    print("item exists in the list")
else:
    print("item does not exist in the list")  
print(cars)
print("the total items in car list:\t",len(cars))
