"""cars=["benz","audi","toyota","lexus","rangerover"]
print(cars[2:])
"""
phone=(("4","true","samsung","5","true"))
#this is a list constructor
books=list(("kasuku","star","kartasi","superstar"))
print(books)

#to change a list 
a=["1","2","3","4","5"]
a[1]="accumulator"
print(a)
#to test if a list is present
cars=["audi","benz","range","lexus"]
if "benz"  in cars:
     print("yes,'benz',is in the cars")
     #to chenge two values in a list
"""cars=["audi","benz","range","lexus"]
cars[1:3]=["toyota","daisy"]
print(cars)
#to change one value with multiple values
cars=["audi","benz","range","lexus"]
cars[1:2]=["toyota","daisy"]
print(cars(len))
#replacin multiple list items with one item
cars=["audi","benz","range","lexus"]
cars[1:3]="accumulator"
print(cars)
"""
#inserting a new item in the list
cars=["audi","benz","range","lexus"]
cars.insert(3,"benzoo")
print(cars)
#how to append
cars=["audi","benz","range","lexus"]
cars.append("bmw")
print(cars)
#hoe to extend a list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#to add a tuple to a list
thislist = ["apple", "banana", "cherry"]
tropical = ("mango", "pineapple", "papaya")
thislist.extend(tropical)
#to remove an item in a list
thislist = ["apple", "banana", "cherry"]
thislist.remove("apple")
print(thislist)
#pop remove
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#using del to remove an item
thislist = ["apple", "banana", "cherry"]
del thislist [1]
print(thislist)
#pop remove the last
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#using del to remove an item
thislist = ["apple", "banana", "cherry"]
del thislist 
print(thislist)
                                          









