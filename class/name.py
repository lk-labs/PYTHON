class person:
 def __int__(self,w,h,g):
     self.weight=w
     self.heght=h
     self.gender=g

 def viewperson(self):
     print('Weight :',self.weight,'Height is :',self.heght,'Gender :',self.gender)

p=person("67kgs","45ft","Male")
p.viewperson()