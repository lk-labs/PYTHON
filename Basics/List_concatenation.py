cars=["Voxy","Noah","Audi","Rollsroyce","Benz"]

cars_2=["range","lexus","ford"]

cars.extend(cars_2)

for car in cars:
    print(car)
    
print("\n")


#looping through cities
cities=["Nairobi","mombasa","Nakuru","kisumu","eldoret"]
for city in cities:
    print(city)

print("\n")

#looping through the index
for city in range(len(cities)):
    print(city)

print("\n")

#sorting a list
cities=["Nairobi","mombasa","Nakuru","kisumu","eldoret"]
cities.sort()
print(cities)

towns=cities.copy()


