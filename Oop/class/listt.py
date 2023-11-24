cars=["volo","passat","vitz","bmw","toyota"]
print(len(cars))
print(type(cars))
print(cars[-1])
print(cars[1])
print(cars[-2])
print(cars[0:2])
print(cars[2:4])
print(cars[1:])
print(cars[3:])
print(cars[2:4])
print(cars[-1:-3])
cars.insert(1,"mazda")
print(cars)
cars_2=["benz","isuzu","suzuki"]
cars.extend(cars_2)
print(cars)
cars.append("lexus")
print(cars)
cars.remove("mazda")
print(cars)
cars.pop()
print(cars)
#checking present cars
if "isuzu" in cars:
    print("yes it is present")
else:
    print("no ")  

#looping through a list
for car in cars:
    print(cars)      