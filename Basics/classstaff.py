class person:
    def __init__(self):
        self.name=input("ebter your name:")
        self.gender=input("enter the gender:")
        self.date=input("ennter the date of birth:")
        self.height=int(input("enter your height:"))
class staff(person):
    def dep_salary(self):
        self.department=input("enter your department:")
        self.salary=int(input("enter the salary :"))
    def view_person(self):
        print(f"name:{self.name}")  
        print(f"gender:{self.gender}")
        print(f"date:{self.date}")
        print(f"height:{self.height}")
        print(f"department:{self.department}")
        print(f"salary:{self.salary}")

s=staff()
s.dep_salary()
s.view_person()                  