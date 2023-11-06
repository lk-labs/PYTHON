#tuple constructor
#fruits=tuple(("apples","mangoes","oranges","Berries"))
#print(fruits)
#to count the total items in a tuple
#print("total items in fruits is\t",len(fruits))
#prints the type of data type
#print(type(fruits))
#accessing a tuple using index
"""print(fruits[1])
print(fruits[-2])
print(fruits[1:3])
print(fruits[1:4])
print(fruits[1:])
print(fruits[:-2])
"""
# checking if an item exists
#searchvar=input("enter a value to search for :\n")
#if searchvar in fruits:
"""print("yes ,items exists in the tuple")
else:
    print("no ,item does not exist in tuple") 
    """
#type conversion to list

mypc=("Hp","16 GB RAm","500GB HD","200,000")
#convert a tuple into a list
mylist=list(mypc)
#modifying the list by adding cpu speeed on position 2
mylist.insert(1,"Icore 7 ,gen 12")
#convert back to tuple
mypc=tuple(mylist)
print(mypc)





