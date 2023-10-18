class Person:
    def __int__(self, w, h, g):
        self.weight = w
        self.heght = h
        self.gender = g

    def viewPerson(self):
        print('Weight :', self.weight, 'Height is :', self.heght, 'Gender :', self.gender)


p = Person("67kgs", "45ft", "Male")
p.viewPerson()
