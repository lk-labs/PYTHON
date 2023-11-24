class person:
    def capture(self):
        self.name=input("enter person name:")
        self.gender=input("enter the gender of the person:")
        self.height=input("enter the height of the person:")
        self.weight=input("enter the weight of the person:")
class student(person):
    def registration(self):
        self.regno=input("enter the student registration number:")
        self.dep=input("enter student department:")
    def view_person(s):
        print(f"regno:{s.regno}  name:{s.name} gender:{s.gender} department:{s.dep} gender:{s.gender}height:{s.height} weight:{s.weight}")  

S=student()
S.capture()
S.registration() 
S.view_person()         

