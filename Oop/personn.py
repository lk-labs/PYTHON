class person:
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
    def display(self):
        print("name",self.name)
        print("age",self.age)
        print("weight",self.weight)
        print("height",self.height)
p=person("malcom","12","30","10")
p1=person("brian","21","70","90")
print("properties of p\n")
p.display()
print("properties for p1\n")
p1.display()            
        