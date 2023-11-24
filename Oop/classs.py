class person:
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height

    def display(self):
        print(f"name :{self.name} age: {self.age} weight:{self.weight} height:{self.height}") 
name=input("enter your name:")
age=int(input("enter your age:"))
weight=int(input("enter your weight:"))
height=int(input("enter your height:")) 
p=person(name,age,weight,height)
p.display()          