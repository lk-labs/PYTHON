class person:
    def capture_person(self):
        self.name=input("enter your name:")
        self.gender=input("enter your gender:")
        self.height=int(input("enter the height:"))
        self.weight=int(input("enter the weight:"))
class student(person):
    def registration(self):
        self.reg=int(input("enter your registration number:"))
        self.department=input("enter the name of department:")
    def view(self):
        print("name",self.name)
        print("reg",self.reg)
        print("gender",self.gender)
        print("height",self.height) 
        print("weight",self.weight)
        print("department",self.department)              
s=student()
s.capture_person()
s.registration()
s.view()        