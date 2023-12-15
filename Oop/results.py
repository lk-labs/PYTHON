class student:
    def __init__(self,regno):
        self.regno=regno
        
class results(student):
    def __init__(self, regno,english_mark,math_mark):
        super().__init__(regno)    
        self.english_mark=english_mark
        self.math_mark=math_mark 

    def        