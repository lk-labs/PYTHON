#Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered, unchangeable*, and unindexed.

#Note: Set items are unchangeable, but you can remove items and add new items.

#Sets are written with curly brackets.

thisset = {"apple", "banana", "cherry"}
print(thisset)

#Unordered
#Unordered means that the items in a set do not have a defined order.

#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

#Unchangeable
#Set items are unchangeable, meaning that we cannot change the items after the set has been created.

#True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#getting the len of the  set we use len ()

thisset={"volv0","benz","mazda"}
print(len(thisset))

#set items can be of any data type
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

# a set can be of many data type
set1 = {"apple", "banana", "cherry","1","2","false"}
print(set1)
#to know the type of data type we use type()
set1 = {"apple", "banana", "cherry"}
print(type(set1))

#set constructor
set1 =set( ("apple", "banana", "cherry","1","2","false"))
print(set1)
#accessing items in a set
set1 = {"apple", "banana", "cherry","1","2","false"}
for x in set1:
    print(x)
 #using range len ()
set1={"apple","mango","banana","sweetmelon"}
for x in range(len(set1)):
    print(set1)    

#using while loop
set1={"apple","mango","banana","sweetmelon"}
i=0
while i < len(set1):
    print(set1)
    i=i+1

#checking presence of an item you use if then in\
set1={"apple","mango","banana","sweetmelon"}
if "apple" in set1:
    print("yes,'apple' is present in the set")
else:
    print("no,'apple' is not present") 

    # addin an item  use add1()
set1={"apple","mango","banana","sweetmelon"}
set1.add("orange")
print(set1)

#using update ()
fruits={"apple","mango","banana","sweetmelon"}
tropical={"passion","pineapple","avacado"}
fruits.update(tropical)
print(fruits)

# using update with a different data type
fruits={"apple","mango","banana","sweetmelon"}
tropical=["passion","pineapple"]
fruits.update(tropical)
print(fruits)

#to remove an item use remove ()
fruits={"apple","mango","banana","sweetmelon"}
fruits.remove("apple")
print(fruits)

#using discard method to remove an item
fruits={"apple","mango","banana","sweetmelon"}
fruits.discard("mango")
print(fruits)

#using pop() to remove a random item
fruits={"apple","mango","banana","sweetmelon"}
x=fruits.pop()
print(x)
print(fruits)

#using clear function emptes the set
fruits={"apple","mango","banana","sweetmelon"}
fruits.clear()
print(fruits)
"""The del keyword will delete the set completely:
fruits={"apple","mango","banana","sweetmelon"}
del fruits
print(fruits)
"""
#looping a set
#for loop
cars={"volvo","benz","v8","mazda"}
for car in cars:
    print(car)

#while loop
cars={"volvo","benz","v8","mazda"}
i=0
while i < len(cars):
    print(cars)
    i=i+1

#using range len()

cars={"volvo","benz","v8","mazda"}
for x in range(len(cars)):
    print(cars)

#to join sets you use update () and  union function ()
cars={"volvo","benz","v8","mazda"}
cars_2={"lexus","toyota","bmw"}
cars.update(cars_2)
print(cars)

# using union ()
cars={"volvo","benz","v8","mazda"}
cars_2={"lexus","bmw"}
cars_3=cars.union(cars_2)
print(cars_3)

#the intersection_update() method will keep only the items that are present in both sets.
cars={"volvo","benz","v8","mazda"}
cars_2={"lexus","bmw","v8","mazda"}
x=cars.intersection(cars_2)
print(x)

#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
cars={"volvo","benz","v8","mazda"}
cars_2={"lexus","bmw","v8","mazda"}
cars.symmetric_difference_update(cars_2)
print(cars)
#the symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
cars={"volvo","benz","v8","mazda"}
cars_2={"lexus","bmw","v8","mazda"}
x=cars.symmetric_difference(cars_2)
print(x)

#set methods
"""Method	Description
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
"""



   





  



















































































































































