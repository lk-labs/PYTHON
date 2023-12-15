class person:
    def capture(self):
        self.name=input("enter your name\n") 
        self.weight=int(input("enter your weight:"))
        self.gender=input("enter your gender") 

    def write(self):
        print(f"name:{self.name}")
        print(f"weight:{self.weight}")
        print(f"gender:{self.gender}")   

s=person()
s.capture()
s.write()          