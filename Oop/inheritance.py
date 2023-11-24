class student:
    def __init__(self,name,weight,height):
        self.name=name
        self.height=height
        self.weight=weight

    def view(self):
        print(self.name,self.height,self.weight)

class person(student):
    pass
x=student("john","20ft","69")  
x.view()          


