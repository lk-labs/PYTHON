class Person:
 def __init__(self,name,w,h,g):
     self.name=name
     self.weight=w
     self.height=h
     self.gender=g
 def viewPerson(self):
     print(self.name,self.weight,self.height,self.gender)
p=Person("Joe","62.5 Kgs","6 FT","Male")
p.viewPerson()