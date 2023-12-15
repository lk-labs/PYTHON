class person:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height
    def display(self):
        print("name",self.name)
        print("weight",self.weight)
        print("height",self.height)
p=person("lucy","40 kg","20 ft") 
p.display()
