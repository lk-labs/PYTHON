thisdict={
    "name": "lucy",
    "reg_no": "1045121",
    "course": "computer science" ,
    "department":"computer science",
    "unit": "cmt 208"

}
print(thisdict)
# Dictionary items are ordered, changeable, and does not allow duplicates.
#how to acesss individual item

print(thisdict["name"])
print(thisdict["course"])

#no duplicates are allowed ,,it overwrites

thisdict={
    "name": "lucy",
    "reg_no": "1045121",
    "course": "computer science" ,
    "department":"computer science",
    "unit": "cmt 208",
    "unit": "cmt 203"

}
print(thisdict)

#len of dict
print(len(thisdict))

#data type
print(type(thisdict))
#supports any data type
#constructor
thisdict=dict( name="lucy",reg_no="1045121",department="computer science")
print(thisdict)
#The keys() method will return a list of all the keys in the dictionary.
thisdict={
    "name": "lucy",
    "reg_no": "1045121",
    "course": "computer science" ,
    "department":"computer science",
    "unit": "cmt 208",
    "unit": "cmt 203"

}
x=thisdict.keys()
print(x)
thisdict["age"]="20"
print(x)
print(thisdict)

#getting the values of dict
x=thisdict.values()
print(x)
thisdict["sex"]="female"
print(x)
print(thisdict)
#using get method
print(thisdict.get("age"))

#getting items in a dictionary

x=thisdict.items()
print(x)
thisdict["group"]="A"
print(x)

#checking if a key exists

if "love" in thisdict:
    print("yes,age,exists in thisdict")
else:
    print("no")   

 #You can change the value of a specific item by referring to its key name:

thisdict["age"]=21 
print(thisdict) 

#update the keys using update() 
thisdict.update({"reg_no":1045858})
print(thisdict)

#removing an item
#using pop()

thisdict.pop("age")
print(thisdict)

#removing a random item using popitem (),removes the last item
thisdict.popitem()
print(thisdict)

"""#del key deletes the whole set
del thisdict
print(thisdict)
"""

"""#clear key empties a set
thisdict.clear()
print(thisdict)
"""
#looping through a dict
for x in thisdict:
    print(x)
 #using while loop 

keys = list(thisdict.keys())
i=0

while i < len(keys):
    key = keys[i]
    value = thisdict[key]
    print(f"{key}: {value}")
    i += 1
#printing one alue
#not all values in the dictionary, one by one:

"""for x in thisdict:
  print(thisdict[x])
  """
#for keys
for x in thisdict.keys():
    print(x)

#for values

for x in thisdict.values():
    print(x)
#looping through both keys and values

for x in thisdict.items():
    print(x)
 # copying items using copy()
mydict=thisdict.copy()
print(mydict)
    #using dict()
mydict=dict(thisdict)  
print(mydict)  
#nested dictionaries

child1 ={
         "name": "lucy",
         "age":  18,
         "year": 2001
                            
         }

child2 ={
         "name": "caro",
         "age": "15",
         "year": 2009,

        }

child3 = {
           "name": "emma",
           "age" : 11,
           "year": 2014
         }
        

myfamily= {
                "child1": child1,
                "child2": child2,
                "child3": child3,
            }
print(myfamily)

""""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""
