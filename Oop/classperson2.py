class person:
    def __init__(self):
        self.name=input("enter your name:")
        self.age=int(input("enter your age:"))
        self.weight=int(input("enter your weight:"))
        self.height=int(input("enter your height:"))

    def display(self):
        print(f"name:{self.name}  age:{self.age}  weight:{self.weight}   height:{self.height}")    


p=person()
p.display()        
        