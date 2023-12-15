class person:
    def capture_person(self):
        self.name=input("enter your name:")
class department:
    def dep_information(self):
        self.department=input("enter your department:")
class staff(person,department):
    def capture_staff(self):
        self.staffno=int(input("enter the staff number:"))
    def view(self):
        print("name",self.name)
        print("staffno",self.staffno)
        print("department",self.department)
        print("staffno",self.staffno) 
s=staff()
s.capture_person()
s.dep_information()
s.capture_staff()
s.view()           
