class student:
    def __init__(self):
     self.regno=int(input("enter your regno :"))
class results(student):
    def __init__(self):
        super().__init__() 
        self.englishmark=int(input("enter your marks:"))
        self.mathmark=int(input("enter your math mark:"))
        self.totalmark=self.calculate_total_mark()
    def calculate_total_mark(self):
        return self.englishmark+self.mathmark  
    def view(self):
        print(f"regno:{self.regno} englishmak:{self.englishmark} mathmark:{self.mathmark} totalmark:{self.totalmark}")     
s=results()
s.calculate_total_mark()
s.view()