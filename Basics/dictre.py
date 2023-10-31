thisdict={
   " Regno":"104121",
   "name"  : "lucy" ,
   "age"   : "20",
   "course" : "computer science",
   "faculty" : "science",
   "year"   :  "2003",
   "unit"   : "cmt 210",
   "unit_name":"oop1"
}
#print(thisdict)
#x=thisdict.keys()
#print(x)
#x=thisdict.values()
#print(x)

thisdict["age" ]="21"
print(thisdict)
thisdict["year"]="2000"
print(thisdict)

print(thisdict.get("age"))
print(thisdict.get("course"))

x=thisdict.items()
print(x)



#updating items

#x=thisdict.update({"id number":3991702})
#print(thisdict)

x=thisdict.update({"lec":"wendy"})
print(x)
                   

























