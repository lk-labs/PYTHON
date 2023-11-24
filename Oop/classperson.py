class person:
     def __init__(self,name,age,weight,height):
          self.name=name
          self.age=age
          self.weight=weight
          self.height=height

     def display(self):
          print(f"name:{self.name}  age:{self.age}   weight:{self.weight}  height:{self.height}")

p=person("lucy","20","60 kg","20 ft")
print("properties of p\n")
p.display()
p1=person("mercy","30","90 kg","45 ft") 
print("propertie of object p1\n")
p1.display()               