class person:
    def capture_person(self):
        self.name=input("enter the name of person:")
class department :
    def capture_department(self):
        self.dep=input("enter the department name:")
class staff(person,department):
    def capture_staff(self):
        self.staffnumber=input("enter staff number:")
    def view(self):
        print(f"staffno:{self.staffnumber} name:{self.name} department:{self.dep}")    
s=staff()  
s.capture_person()              
s.capture_staff()
s.capture_department()
s.view()