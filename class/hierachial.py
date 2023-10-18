class person:
    def details(self):
        self.name=input('Enter name \n ')
        self.gender=input('Enter the gender \n')
        self.height=input('Enter height \n')

class student(person):
    def Regno(self):
        self.Regno=input('Enter student number \n')

class staff(person):
    def staffId(self):
        self.staffId=input('Enter staffId \n')

# creat objects
s=student()
s.Regno()
s.details()
s1=staff()
s1.staffId()
s1.details()
print('Print information for student \n')
print(s.Regno,s.name,s.height,s.gender)
print('Print information for staff \n')
print(s1.sId,s1.name,s1.gender,s1.height)
