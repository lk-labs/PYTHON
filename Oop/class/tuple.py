fruits=("banana","apple","mango","pineapple","watermelon")

# to change into a list
fruit_list=list(fruits)

# items to be added
List_add=("passion","avacado")

#adding items 
fruit_list.extend(List_add)

#type convertion of list into tuple
fruits=tuple(fruit_list)


print(fruits)
#inserting an item
fruits=("banana","apple","mango","pineapple","watermelon")
fruits_1=list(fruits)
fruits_1.insert(0,"potatoe")
fruits=tuple(fruits_1)
print(fruits)
#to append 
fruits=("banana","apple","mango","pineapple","watermelon")
fruits_1=list(fruits)
fruits_1.append(0)
fruits_1=tuple(fruits)
print(fruits)

#unpacking tuple


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
# asterik
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)




##unpacking tuples
fruits = ("apple", "mango", "papaya","pineapple", "cherry","apple")

(orange,purple,*red)=fruits
print(orange)
print(purple)
print(red)
# looping through tuples


fruits = ("apple", "mango", "papaya","pineapple", "cherry","apple")
for x in fruits:
    print(x)

#you can also loop through the tuple items by referring to their index number.

#Use the range() and len() functions to create a suitable iterable.

fruits = ("apple", "mango", "papaya","pineapple", "cherry","apple")
for x in range(len(fruits)):
    print(fruits[x])
    
#Using a While Loop
#You can loop through the tuple items by using a while loop.

#Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.

#Remember to increase the index by 1 after each iteration.

fruits = ("apple", "mango", "papaya","pineapple", "cherry","apple")
i=0
while i < len(fruits):
    print(fruits[i])
    i=i+1

    #joining tuples
    # To join two or more tuples you can use the + operator:
    fruits = ("apple", "mango", "papaya","pineapple", "cherry")
    fruits_1=("watermelon","passion")
    fruits_2=fruits+fruits_1
    print(fruits_2) 

    #Multiply Tuples
#If you want to multiply the content of a tuple a given number of times, you can use the * operator:
#Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)  

#tuple methods
"""Tuple Methods
Python has two built-in methods that you can use on tuples.

Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""
#count ()method
fruits = ("apple", "banana", "cherry","apple")
count_apple=fruits.count("apple")
print(count_apple)
print(fruits)

#index method
fruits = ("apple", "banana", "cherry","apple")
fruits_index=fruits.index("banana")
print(fruits_index)
print(fruits)



