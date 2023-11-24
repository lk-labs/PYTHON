class person:
    def __int__(self, n):
        self.name = n
class department:
    def staffDepartment(self):
        self.department=input('\n Enter department \n')
class staff(person , department):
    def __int__(self, n):
        person.__int__(self, n)
    def staffId(self):
        self.sId=input('Enter staff Id')
# create staff object
name = input('Enter staff name ')
s = staff(name)
s.staffDepartment()
s.staffId()
print(s.Id , s.name , s.name)