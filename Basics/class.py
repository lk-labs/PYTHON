class person:
    def capture(self):
        self.name=input("enter your name:")
        self.gender=input("enter your gender:")
        self.height=input("enter your height:")
        self.weight=input("enter your weight:")
class student(person):
    def registration(self):
        self.regno=int(input("enter your registration number:"))
        self.dept=input("enter the name of your department:")
    def view(self):
        print(f"name:{self.name}  gender:{self.gender} regno:{self.regno} height:{self.height} weight:{self.weight} department:{self.dept}")
s=student()
s.capture()
s.registration()
s.view()        

    
     