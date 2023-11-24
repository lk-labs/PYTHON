class lecturer:

    def __init__(self,name,gender,unit):
        self.name=name
        self.gender=gender
        self.unit=unit

    def view(self):
        print(self.name)
        print(self.gender)
        print(self.unit)   

class student(lecturer):
    def __init__(self, name, gender, unit,year):
        super().__init__(name, gender, unit)
        self.graduation=year

    def welcome(self): 
        print("welcome",self.name,"to the class of",self.graduation)   
x=student("john","female","cmt 203",2023) 
x.welcome()

     

        