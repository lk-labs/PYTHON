class person:
    def __init__(self,name,age,weight,height):
        self.name=input
        self.age=age
        self.weight=weight
        self.height=height

    def display(self):
        print(f"name:{self.name}  age:{self.age} weight:{self.weight}  height:{self.height}")  
p=person("lucy","23","40","34")
p.display()          