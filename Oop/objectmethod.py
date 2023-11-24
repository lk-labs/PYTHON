class mystudent():
    def __init__(self,name,age,faculty):
        self.name=name
        self.age=age
        self.faculty=faculty
        def myfunc(self):
          print("my name is "+ self.name)        
pi=mystudent("john",15,"science")
pi.myfunc()  